#include <bits/stdc++.h>

using namespace std;

struct node {
	int r;
	int adj[20][20];
	int col[20];
	int dig1[40];
	int dig2[40];
};

int feasible(node p, int c, int n) {
	if(p.col[c] == 1) {
		return 0;
	}
	if(p.dig1[p.r + c] == 1) {
		return 0;
	}
	if(p.dig2[p.r - c + n] == 1) {
		return 0;
	}
	return 1;
}
void nqueen(int r, int n) {
	queue <node> q;
	int i, j;
	node temp;
	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++) {
			temp.adj[i][j] = 0;
		}
		temp.col[i] = 0;
	}
	for(i = 0; i < 2 * n; i++) {
		temp.dig1[i] = temp.dig2[i] = 0;
	}
	temp.r = 0;
	q.push(temp);
	while(!q.empty()) {
		node p = q.front();
		q.pop();
		if(p.r == n) {
			for(i = 0; i < n; i++) {
				for(j = 0; j < n; j++) {
					cout << p.adj[i][j] << " ";
				}
				cout << endl;
			}
			break;
		}
		for(i = 0; i < n; i++) {
			if(feasible(p, i, n)) {
				p.adj[p.r][i] = 1;
				p.col[i] = 1;
				p.dig1[p.r + i] = 1;
				p.dig2[p.r - i + n] = 1;
				p.r = p.r + 1;
				q.push(p);
				p.r = p.r - 1;
				p.adj[p.r][i] = 0;
				p.col[i] = 0;
				p.dig1[p.r + i] = 0;
				p.dig2[p.r - i + n] = 0;
			}
		}
	}
}
int main() {
	int n;
	cin >> n;
	nqueen(0, n);
	return 0;
}