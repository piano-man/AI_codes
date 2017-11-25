#include <bits/stdc++.h>
#define ff first
#define ss second
using namespace std;

int n;
struct node {
	int lm;
	int lc;
	int pos;
};
struct cmp{
	bool operator()(const node &a, const node &b) {
		if(a.lm == b.lm) {
			if(a.lc == b.lc) {
				return a.pos < b.pos;
			}
			return a.lc < b.lc;
		}
		return a.lm < b.lm;
	}
};
set<node, cmp> s;
map<node, node, cmp> m;
int valid(node p) {
	if(p.lm && p.lc > p.lm) {
		return 0;
	}
	if(p.lm != n && p.lc < p.lm) {
		return 0;
	}
	if(s.find(p) != s.end()) {
		return 0;
	}
	return 1;
}
void print_path(node p) {
	if(p.lc == -1) {
		return;
	}
	print_path(m[p]);
	cout << p.lc << " " << p.lm << " " << p.pos << " " << n - p.lc << " " << n - p.lm << endl;
}
int find_sol(node pr) {
	queue<node> q;
	q.push(pr);
	while(!q.empty()) {
		node  p = q.front();
		q.pop();
		if(p.lc == 0 && p.lm == 0) {
			print_path(p);
			return 1;
		}
		if(p.pos == 0) {
			node p2;
			p2.pos = 1;
			if(p.lm > 0) {
				p2.lm = p.lm - 1;
				if(p.lc > 0) {
					p2.lc = p.lc - 1;
					if(valid(p2)) {
						s.insert(p2);
						m[p2] = p;
						q.push(p2);
					}
				}
				p2.lc = p.lc;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}
			if(p.lc > 0) {
				p2.lc = p.lc - 1;
				p2.lm = p.lm;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}
			if(p.lc > 1) {
				p2.lc = p.lc - 2;
				p2.lm = p.lm;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}	
			if(p.lm > 1) {
				p2.lm = p.lm - 2;
				p2.lc = p.lc;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}
		}
		else {
			node p2;
			p2.pos = 0;
			if(p.lm < n) {
				p2.lm = p.lm + 1;
				if(p.lc < n) {
					p2.lc = p.lc + 1;
					if(valid(p2)) {
						s.insert(p2);
						m[p2] = p;
						q.push(p2);
					}
				}
				p2.lc = p.lc;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}
			if(p.lc < n) {
				p2.lc = p.lc + 1;
				p2.lm = p.lm;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}	
			}		
			if(p.lc < n - 1) {
				p2.lc = p.lc + 2;
				p2.lm = p.lm;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}

			if(p.lm < n - 1) {
				p2.lm = p.lm + 2;
				p2.lc = p.lc;
				if(valid(p2)) {
					s.insert(p2);
					m[p2] = p;
					q.push(p2);
				}
			}
		}
	}
	return 0;
}
int main() {
	cin >> n;
	node temp;
	temp.lc = temp.lm = temp.pos = -1;

	node p;
	p.lc = n;
	p.lm = n;
	p.pos = 0;
	m[p] = temp;
	s.insert(p);
	int ans = find_sol(p);
	return 0;
}