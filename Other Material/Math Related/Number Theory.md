# Lesson 1
- $\color{Lightblue} \textbf{Induction}$
	- Base case: "$n_0$ domino falls“
	- Inductive step: "if $n_0$ domino falls, then $n_{0+1}$ domino will also fall"
	- **EXERCISE 1.1
		- Prove that $1+2+\cdots+n=\frac{n(n+1)}{2}$
		- We‘ll show $P(n)$ true for all $n \ge 1$ by induction.
		- Base case: $P(1): 1= \frac{1(1+1)}{2}$
		- Inductive Step: Suppose $P(n)$ is true for some positive integer $n$. We want to prove $P(n+1)$
		- $1+2+\cdots+(n+1) = [1+ 2 + \cdots + n] + (n+1)$
		- $= \frac{n(n+1)}{2} + (n+1)$
		- $= \frac{n(n+1)+2(n+1)}{2} = \frac{(n+2)(n+1)}{2}$
	- **EXERCISE 1.2
		- Prove that the number $27^{n+1} - 26 n - 27$ is a multiple of $169$ for all positive integers $n$.
		- We'll show $P(n)$ true for all $n \ge 1$ by induction.
		- Base case: $P(1) : 169\  |\ 27^2-26-27=4 \times169$
		- Inductive Step: Suppose $P(n)$ is true for some positive integer $n$. We want to prove $P(n+1)$
		- Let $27^{n+1}-26n-27$ be a multiple of $169$. 
			- Then, $27^{n+2} - 26(n+1)-27 = 27^{n+2}-26n-53$
			- $27(27^{n+1}-26n-27) = 27^{n+2} - 702n - 729$
			- Thus, $27^{n+2}-26(n+1)-27=27(\color{lightblue}27^{n+1}-26n-27\color{white}) + \color{lightblue}169\color{white}(4n+4)$
			- Which is divisible by 169
	- **EXAMPLE: For every integer $n \ge 1$
		- $f_{n-1}f_{n+1} = f_n^2+(-1)^n$
		- Proof: If $n=1$, then $f_0f_2=0$ and $f_1^2+(-1)^1=1-1=0 \color{lightgreen} \ √$ 
		- For the inductive step, $f_nf_{n+2}$ = $f_n(f_n+f_{n+1})$ = $f_n^2+f_nf_{n+1}$
		- = $f_{n-1}f_{n+1} - (-1)^n + f_nf_{n+1}$
		- = $f_{n+1}(f_{n-1}+f_n) + (-1)^{n+1}$
		- = $f_{n+1}^2+(-1)^{n+1}$
		- $\color{Red} \text{NEED REVIEW}$
			- x
- $\color{Lightblue}\textbf{Strong Induction}$
	- **EXAMPLE 1.5![[2e02d74571b524228f4ba591651383d 3.png]]
	- "Build Good Numbers from previous obtained good numbers"
	- $2n+9 \text { and } 2n+8 \text{ are both good}$
	- 巧妙！
- $\color{Lightblue} \textbf{Well-Ordering Principle}$
	- Let $\mathbb{N} = \{0,1,2,\cdots\}$  ->  $\text{Every non-empty subset of } \mathbb{N} \text{ has a smallest element}$
	- **EXAMPLE 1.6
		- Prove that $\sqrt{2}$ is irrational.
		- Proof 1: Suppose $\sqrt{2} = \frac{a}{b}$ for some positive integers $a$ and $b$.
		- ![[Pasted image 20250610002824.png]]
		- ？？？？？？$\color{RED} \text{NEED REVIEW}$
	- ![[Pasted image 20250610004916.png]]
	- 初始条件：n=1 1+x >= 1x+x √
	- 其次：n=n+1 (1+x)(1+x)^n >= 1+nx+x
	-  (1+x)^n - nx - 1 >= 0
	- (1+x)(1+x^n)-1-(n+1)x >= 0
	- (1+x)(1+x^n-nx-1) -> (1+x)(1+x)^n - nx - nx^2 -1 - x +nx^2 <- nx^2 is positive, QED!
	- ![[Pasted image 20250610005414.png]]
	- My Conjecture is it can be divided by 3^n where n = 0,1,2,3,4,...
	- we know that 1 is okay, so.... 
	- we know 16^n - 1 = $k_1n$
	- How do we prove $16^{3n} - 1$ = $k_1k_23n$?
	- (16^n)^3 - 1 = $(a-b)(a^2+ab+b^2)=(16^n-1)(16^2n+16^n+1)
	- => Prove that 3 | (16^2n + 16^n + 1)
	- => Remainder 1 + 1 + 1 = 3 | 3 -> yey
	- ![[Pasted image 20250610010110.png]]
	- 27 > 16 4
	- 3^27 > 2^16 4^4
	- 3^3^27 >2^2^16 4^4^4
	- 3^3^3^27
	- 2^2
	- 2^8
	- 2^2^9
	- $a_2 > b_1$
	- $3^{a_2}$ > $4$
	- a_{n+1} > 2b_n
	- a_2 > 2b_1
	 a_k+1 > 2b_k
	- 3^2 > 2* 4^{b_k}
	- 
	- $a_3$ > 2$b_2$ $log_3 {4}$ 

# Lesson 2
- $\color{Lightblue} \text{Definition}$
	- An arithmetic function is a function $f$: $\mathbb{Z^+} \rightarrow \mathbb{C}$
		- An arithmetic function $f$ is additive if $f(m+n) = f(m)+f(n)$ for all pairs $(m,n)$ with $\gcd(m,n) = 1.$
		- An arithmetic function $f$ is multiplicative if $f(m+n) = f(m)f(n)$ for all pairs $(m,n)$ with $\gcd(m,n) = 1.$
- $\color{Lightblue} \text{Examples:}$
	- $1(n)=1$ and $id(n)=n$ are both multiplicative.
	- Prime counting function $\omega(n)$
		- $$\omega(n)=\sum_{p | n} 1 = \# \text{ of distinct prime divisors of } n$$
		- $p$ is prime, Note $omega$ is additive
		- $\omega(12) = 2 = \omega(3) + \omega(4)$
	- $\Omega(n)$ is defined by
		- $$\Omega(n)=\sum_{p^\alpha || n} \alpha= \# \text{ of prime divisors with multiplicity}$$
	- For any complex number $k$, we may define
		- $$d_k(n) = \sum_{d|n} d^k$$
		- (sum is over divisors d of n)
		- $d_2(12)=1^2+2^2+3^2+4^2+6^2+12^2$
		- $\textit{Turns out }$$d_k$ $\textit{is multiplicative!}$
	- The Mobius function $\mu(n)$ is defined by:
		$\begin{cases} 0 \hspace{1em} &\text{if n divisible by square of prime}\\ (-1)^k \hspace{1em} &\text{if n = } p_1, p_2, p_3, \cdots \end{cases}$
		- This is multiplicative
- ![[Pasted image 20250610232421.png]]
	- $\sigma(n)\varphi(n) = \sigma(p_1^{\alpha_1})\sigma(p_2^{\alpha_2})\cdots\sigma(p_k^{\alpha_k})\varphi(p_1^{\alpha_1})\varphi(p_2^{\alpha_2})\cdots\varphi(p_k^{\alpha_k})$ 
	- $=\sigma(p_1^{\alpha_1})\sigma(p_2^{\alpha_2})\cdots\sigma(p_k^{\alpha_k})\cdot$
- ![[Pasted image 20250610233831.png]]
- ![[Pasted image 20250610234918.png]]
- ![[Pasted image 20250610235559.png]]
- ![[Pasted image 20250611000328.png]]

# Lesson 3
![[Pasted image 20250611231749.png]]
![[Pasted image 20250611232316.png]]

# Lesson 4
- $\color{Lightblue} 4.1.1 \text{ Proposition}$
	- 1. $a \equiv a \text{ (mod n)}$
	- 2. $a \equiv b \text{ (mod n)} \Leftrightarrow b \equiv a \text{ (mod n)}$
	- 3. $a \equiv b \text{ (mod n)}, b \equiv c \text{ (mod n)} \Rightarrow a \equiv c \text{ (mod n)}$
	- 4. $a \equiv c \text{ (mod n)}, b \equiv d \text{ (mod n)} \Rightarrow a+b \equiv c+d \text{ (mod n)}$
	- 5. $a \equiv c \text{ (mod n)}, b \equiv d \text{ (mod n)} \Rightarrow ab \equiv cd \text{ (mod n)}$
	- 6. $a \equiv b \text{ (mod n)} \Rightarrow a^n \equiv b^n \text{ (mod n) , } n \in \mathbb{N}$
	- 7. $a \equiv b \text{ (mod n)},$ $P(x)$ is an integer coefficient polynomial, then $P(a) \equiv P(b) \text{ (mod n)}$
- $\color{Lightblue} 4.1.2 \text{ Theorem: Division in Modular Arithmetic}$
	- Let $a, b, c, n \in \mathbb{N^+}$, let $d = \gcd(c, n)$. If $ac \equiv bc \text{ (mod n)}$, then $a \equiv b \text{ (mod n/d)}$.
	- If $d = 1$, then $ac \equiv bc \text{ (mod n)} \Rightarrow a \equiv c \text{ (mod n)}$
- $\color{Lightblue} 4.1.3 \text{ 猎奇区榜首 Example}$
	- Prove that $$\sum_{k=0}^{6n+2}\binom{6n+2}{2k}3^k \equiv \begin{cases}0 &\text{ (mod }3^{n+2}) \hspace{1em} \text{if n is even} \\ 2^{3n+1} &\text{ (mod } 3^{n+2})\hspace{1em} \text{if n is odd}\end{cases} $$
# Lesson 5 Theorems in modular arithmetic
- $\color{lightblue} 5.1.1 \text{ Fermat's Little Theorem}$
	- Let $p$ be a prime not dividing $a$. Then, $a^{p-1} \equiv 1 \text{ (mod p)}$
	- $\textbf{Proof: }$ 
		- Recall that $ax \equiv ay \text{ (mod p)}$ if $a \nmid p$
		- Thus, $\{1, 2, 3, \cdots, (p-1)\} \equiv \{a, 2a, 3a, \cdots, (p-1)a\} \text{ (mod p)}$
		- Which is a bijection between these two sets, now, we multiply every element in each sets:
		- $(p-1)! \equiv a^{p-1}(p-1)! \text{ (mod p)}$
		- Since $p \nmid p-1$
		- Thus, We can deduce that $a^{p-1} \equiv 1 \text{ (mod p)}$
	- Two natural attempts at generalization
		- 1. If $a^n \equiv a \text{ (mod n)}$ for all integer $a$, must $n$ be a prime?
			- No. $a^{561} \equiv 561 \text{ (mod 561)}$ for all $a$. $\textbf{ <- Carmichael Number}$
- $\color{lightblue} 5.1.2 \text{ Definition}$
	- Let $n > 1$
		- 1. The $\varphi(n)$ integers $$1=a_1 <a_2<a_3<\cdots<a_{\varphi(n)}=n-1$$ less than $n$ and relatively prime to $n$ are called the $\textit{canonical reduced residues}$ modulo $n$.
		- 2. A $\textit{reduced residue system}$ modulo $n$ is a set $\varphi(n)$ integers which are incongruent and relatively prime to $n$.
- $\color{Lightblue} 5.1.3 \text{ Euler's Theorem}$
	- Let $n$ be a positive integer, and let $a$ be any integer with $\gcd(a, n) = 1$. Then $a^{\varphi(n)} \equiv 1 \text{ (mod n)}$.
- $\color{Lightblue} 5.1.4 \text{ Wilson's Theorem}$
	- Let $n$ be a positive integer. Then $(n-1)! \equiv -1 \text{ (mod n)}$ if and only if $n$ is prime.
	- $\textbf{Proof: (sketch)}$
		- $(p-1)! = 1 \cdot (p-1) \cdot [2 \cdot 3 \cdot 4 \cdots (p-2)]$
			- $\equiv -[2\cdot 3 \cdot 4 \cdots (p-2)] \text{ (mod p)}$
# Lesson 6
Learned orders.
# Lesson 7
![[Pasted image 20250617235040.png]]
![[Pasted image 20250617235407.png]]
