//Well I guess writting by hand is way better than using AI Prompt... 

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath> 
#include <iomanip>

using namespace std;
const int K = 32; //系数 

struct PlayerRat{
	int Elo;
	int ID;
}; 

int Delta[1009]; 
int N; //总玩家数 
int PElo[1009]; //玩家Elo 下标对应ID 
int CoN;
int ContestID;
int PlayerInfo;
int MatchSize; 
int PRank[26];
string TieString; 

void ChangeRating(int Size, int Rat[], string Tie){
	double Score[26];
	PlayerRat PRat[26];
	double ExpectVal[26]; 
	for(int i = 1; i <= Size; i ++){
		PRat[i].ID = Rat[i];
		PRat[i].Elo = PElo[Rat[i]];
		Score[i] = (double)(Size - i) / (double)(Size - 1);
//		cout << "玩家 " << PRat[i].ID << " 有 " << PRat[i].Elo << " 等级分且排名分数为 " << Score[i] << endl; 
	}
	for(int i = 1; i <= Size; i ++){
		for(int k = 1; k <= Size; k ++){
			if(i == k){
				continue; 
			}else{
				ExpectVal[i] += 1.0 / (1.0 + pow(10, (PRat[k].Elo - PRat[i].Elo) / 400.0)); 
			}
		}
		ExpectVal[i] /= (double)(Size - 1); 
//		cout << "玩家 " << PRat[i].ID << " 的期望分数为" << ExpectVal[i] << endl; 
		Delta[i] = K * (Size - 1) * (Score[i] - ExpectVal[i]);
		PElo[PRat[i].ID] += Delta[i];
	}
}

int main(){
	
	ifstream PlayerFile("datalist.csv");
	
	if (!PlayerFile.is_open()) {
        cerr << "错误：无法打开 datalist.csv 文件！TAT" << endl;
        return 1;
    }
    
	PlayerFile >> N;
	int curPlayerID;
	int curPlayerElo;
	char Seperate;
	for(int i = 1; i <= N; i ++){
		PlayerFile >> curPlayerID >> Seperate >> curPlayerElo;
		PElo[curPlayerID] = curPlayerElo;
	}
	
	cout << "---Elo导入完成owo---" << endl;
	
	ifstream contestFile("Contest.csv");
	
	if (!contestFile.is_open()) {
        cerr << "错误：无法打开 datalist.csv 文件！TAT" << endl;
        return 1;
    }
	
	contestFile >> CoN;

//	cout << CoN << endl;	
//	for(int i = 1; i <= N; i ++){
//		cout << "选手 " << i << " 的Elo评分为 " << PElo[i] << endl;
//	}

	string CurrentContest;

	for(int i = 1; i <= CoN; i ++){
		contestFile >> MatchSize >> Seperate >> ContestID >> Seperate;
		for(int j = 1; j <= MatchSize; j ++){
			contestFile >> PRank[j] >> Seperate;
		} 
		cout << "目前正在处理ID为 " << ContestID << " 的比赛,本次比赛共有 " << MatchSize << " 名玩家参加, 其中涉及到的玩家ID为: ";
		for(int j = 1; j <= MatchSize; j ++){
			cout << PRank[j] << ' ';
		} 
		cout << endl;
		contestFile >> TieString;
		
		ChangeRating(MatchSize, PRank, TieString);
		
		cout << "已完成! 输出新的Elo值: " << endl;
		
		for(int j = 1; j <= MatchSize; j ++){
			cout << "选手 " << PRank[j] << " 的Elo变化为 " << Delta[j] << ", 新的Elo值为 " << PElo[PRank[j]] << endl;
		} 
	}
	
	ofstream dataout("dataout.csv");
	dataout << N << endl;
	for(int i = 1; i <= N; i ++){
		dataout << i << ',' << PElo[i] << endl;
	}

	
	return 0;
} 
