import pulp
import copy
import time

# ==========================================
# Part 1: 逻辑传播与一致性检查 (Python Logic)
# ==========================================

class AkariState:
    def __init__(self, N, M, grid_str):
        self.N = N
        self.M = M
        # 0: No Light (X), 1: Light (L), None: Unknown
        self.assignments = {} 
        self.candidates = []
        self.walls = {} # (r,c) -> number
        self.grid_layout = [] # 存储原始地形 'C', 'W', '0'-'4'

        # 解析输入
        for r in range(N):
            row_layout = []
            for c in range(M):
                char = grid_str[r * M + c]
                row_layout.append(char)
                if char == 'C':
                    self.candidates.append((r, c))
                    self.assignments[(r, c)] = None # 初始为未知
                elif char.isdigit():
                    self.walls[(r, c)] = int(char)
            self.grid_layout.append(row_layout)

    def get_neighbors(self, r, c):
        """获取 (r,c) 周围合法的候选格坐标"""
        nbs = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.N and 0 <= nc < self.M:
                if self.grid_layout[nr][nc] == 'C':
                    nbs.append((nr, nc))
        return nbs

    def assign(self, r, c, val):
        """尝试赋值，如果与已知冲突则返回 False"""
        current = self.assignments.get((r, c))
        if current is not None:
            return current == val # 如果已经赋值，必须一致
        self.assignments[(r, c)] = val
        return True

    def propagate(self):
        """
        运行逻辑传播 (Section 3 Rules).
        返回: True (状态一致), False (发现矛盾)
        """
        changed = True
        while changed:
            changed = False
            # 1. 检查所有数字墙 (Lemma 3.1 & 3.2)
            for (r, c), limit in self.walls.items():
                nbs = self.get_neighbors(r, c)
                
                # 统计邻居状态
                lights = 0
                unknowns = []
                
                for nr, nc in nbs:
                    val = self.assignments[(nr, nc)]
                    if val == 1:
                        lights += 1
                    elif val is None:
                        unknowns.append((nr, nc))
                
                # 规则 A: 灯数已满 -> 剩余邻居必须为 0 (Wall Exclusion)
                if lights == limit:
                    for nr, nc in unknowns:
                        if not self.assign(nr, nc, 0): return False
                        changed = True
                
                # 规则 B: 剩余空位 == 剩余需求 -> 全部填灯 (Wall Saturation)
                elif lights + len(unknowns) == limit:
                    for nr, nc in unknowns:
                        if not self.assign(nr, nc, 1): return False
                        changed = True
                
                # 规则 C: 矛盾检测
                if lights > limit or lights + len(unknowns) < limit:
                    return False # 甚至无法满足墙的要求

            # 2. 简单的光路互斥 (Local Conflict Check)
            # 如果一个点放了灯，且它能照到的邻近点（无墙阻隔）必须为0
            # 这里为了效率，只检查直接相邻的。完整的全局互斥留给 ILP 或更深层的检查。
            for (r, c), val in list(self.assignments.items()):
                if val == 1:
                    # 上下左右如果有灯，必须为0 (除非中间有墙，这里简化处理直接相邻)
                    # 注意：Akari规则是"视线内不能有灯"。这里做最简单的相邻检查作为快速剪枝。
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        while 0 <= nr < self.N and 0 <= nc < self.M:
                            if (nr, nc) in self.walls or str(self.grid_layout[nr][nc]) in '01234X':
                                break # 撞墙停止
                            if (nr, nc) in self.assignments:
                                # 如果是白格
                                if not self.assign(nr, nc, 0): return False # 被照亮的地方不能放灯
                                # 注意：这里有个逻辑，如果 (r,c) 是灯，它照亮的地方不能放灯。
                                # 但我们不能把那些地方设为 0 吗？
                                # 这里的 assign(0) 其实是说：这个格子"不能放置灯源"。
                                # 它不代表"没有被照亮"，而是代表"x_ij = 0"。这是对的。
                            nr += dr
                            nc += dc
        
        return True

def run_sac(state):
    """
    Singleton Arc Consistency (SAC) - Section 4
    尝试假设每个未知变量的值，如果推导出矛盾，则永久排除该值。
    """
    changed = True
    while changed:
        changed = False
        unknown_vars = [pos for pos, val in state.assignments.items() if val is None]
        
        for r, c in unknown_vars:
            # --- 尝试假设 x = 1 ---
            # 深拷贝当前状态进行模拟
            # 注意：为了效率，实际工程中会用回溯(backtrack)而不是deepcopy，这里为了代码清晰用copy
            state_try_1 = copy.deepcopy(state)
            if not state_try_1.assign(r, c, 1) or not state_try_1.propagate():
                # 推导出矛盾！说明 (r,c) 不能是 1
                # 结论：(r,c) 必须是 0
                print(f"[SAC] Pruned: ({r},{c}) cannot be Light -> Fixed to 0")
                if not state.assign(r, c, 0): return False # 主状态矛盾，无解
                state.propagate() # 立即在主状态上传播新知识
                changed = True
                continue # 状态变了，重新开始循环或继续

            # --- 尝试假设 x = 0 ---
            state_try_0 = copy.deepcopy(state)
            if not state_try_0.assign(r, c, 0) or not state_try_0.propagate():
                # 推导出矛盾！说明 (r,c) 不能是 0
                # 结论：(r,c) 必须是 1
                print(f"[SAC] Pruned: ({r},{c}) cannot be Empty -> Fixed to 1")
                if not state.assign(r, c, 1): return False
                state.propagate()
                changed = True
    
    return True

# ==========================================
# Part 2: 混合求解器 (Hybrid Solver)
# ==========================================

def solve_akari_hybrid(N, M, grid_str):
    start_time = time.time()
    
    # 1. 初始化状态
    state = AkariState(N, M, grid_str)
    
    # 2. Phase 1: 基础逻辑传播
    if not state.propagate():
        print("Contradiction found during initial propagation.")
        return None
    
    # 3. Phase 2: SAC 高级一致性检查
    print("Running SAC (Singleton Arc Consistency)...")
    if not run_sac(state):
        print("Contradiction found during SAC.")
        return None
        
    # 统计 SAC 的效果
    fixed_count = sum(1 for v in state.assignments.values() if v is not None)
    total_count = len(state.candidates)
    print(f"SAC finished. Fixed {fixed_count}/{total_count} variables ({(fixed_count/total_count)*100:.1f}%).")

    # 4. Phase 3: 残差 ILP (Residual ILP)
    # 只对剩下的 Unknown 变量建模，已知的直接作为约束固定
    
    prob = pulp.LpProblem("Akari_Hybrid", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("Light", state.candidates, cat=pulp.LpBinary)
    
    # 目标函数
    prob += pulp.lpSum([x[pos] for pos in state.candidates])
    
    # 添加“预处理固定”的约束
    for pos, val in state.assignments.items():
        if val is not None:
            prob += x[pos] == val, f"Fixed_{pos}"

    # --- 构建常规约束 (同纯 ILP，但求解器会利用 Fixed 约束自动预处理) ---
    
    # 预先计算段 (Segments)
    horiz_segments = {}
    vert_segments = {}
    grid_2d = state.grid_layout

    for r in range(N):
        segment = []
        for c in range(M):
            if grid_2d[r][c] == 'C': segment.append((r, c))
            else:
                for pos in segment: horiz_segments[pos] = segment
                segment = []
        for pos in segment: horiz_segments[pos] = segment

    for c in range(M):
        segment = []
        for r in range(N):
            if grid_2d[r][c] == 'C': segment.append((r, c))
            else:
                for pos in segment: vert_segments[pos] = segment
                segment = []
        for pos in segment: vert_segments[pos] = segment

    # 冲突约束
    unique_segments = []
    seen_ids = set()
    for pos in state.candidates:
        for seg in [horiz_segments.get(pos, []), vert_segments.get(pos, [])]:
            if not seg: continue
            seg_id = (seg[0], seg[-1], len(seg)) # 简单hash
            if seg_id not in seen_ids:
                seen_ids.add(seg_id)
                unique_segments.append(seg)
    
    for seg in unique_segments:
        prob += pulp.lpSum([x[pos] for pos in seg]) <= 1

    # 覆盖约束
    for pos in state.candidates:
        # 如果这个格子已经被预处理确定是 1，或者被确定是 0 但已经被预处理的灯照亮，
        # 其实这个约束对于 ILP 来说是多余的，但为了保险还是加上。
        # 优化：如果 pos 已经是 Light，这个约束自动满足 x_pos >= 1。
        visible = set(horiz_segments.get(pos, []) + vert_segments.get(pos, []))
        prob += pulp.lpSum([x[p] for p in visible]) >= 1

    # 墙壁约束
    for (r, c), limit in state.walls.items():
        nbs = state.get_neighbors(r, c)
        prob += pulp.lpSum([x[n] for n in nbs]) == limit

    # 求解
    print("Starting ILP solver for residual problem...")
    solver = pulp.PULP_CBC_CMD(msg=False)
    status = prob.solve(solver)
    
    print(f"Total Time: {time.time() - start_time:.4f}s")

    if pulp.LpStatus[status] == 'Optimal':
        solution = []
        for pos in state.candidates:
            if pulp.value(x[pos]) > 0.5:
                solution.append(pos)
        return solution
    else:
        return None

if __name__ == "__main__":
    # 测试一个包含逻辑陷阱的例子 (需要推理才能解，单纯贪心会挂)
    # 4 墙壁在中间，迫使周围全亮
    # C C C
    # C 4 C
    # C C C
    N = 3
    M = 3
    grid_input = "CCC" + "C4C" + "CCC"
    
    print(f"Hybrid Solving {N}x{M}")
    result = solve_akari_hybrid(N, M, grid_input)
    
    if result:
        print("Solution:", sorted(result))
        # Visual
        grid_list = list(grid_input)
        for r, c in result:
            grid_list[r * M + c] = 'L'
        for i in range(N):
            print(" ".join(grid_list[i*M : (i+1)*M]))
    else:
        print("Unsolvable")
