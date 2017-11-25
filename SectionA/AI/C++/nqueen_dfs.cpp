#include <bits/stdc++.h>

using namespace std;

int adj[50];
int col[50];
int dig1[100];
int dig2[100];


int feasible(int r, int c, int n) {
	if(col[c] == 1) { 
		return 0;
	}
	if(dig1[r + c] == 1) {
		return 0;
	}
	if(dig2[r - c + n] == 1) {
		return 0;
	}
	return 1;
}
int nqueen(int r, int n) {
	if(r == n) {
		int i, j;
		for(i = 0; i < n; i++) {
			for(j = 0; j < n; j++) {
				if(adj[i] == j) {
					cout << "1 ";
				}
				else {
					cout << "0 ";
				}
			}
			cout << endl;
		}
		return 1;
	}
	int i;
	for(i = 0; i < n; i++) {
		if(feasible(r, i, n)) {
			adj[r] = i;
			col[i] = 1;
			dig1[r + i] = 1;
			dig2[r - i + n] = 1;
			if(nqueen(r + 1, n)) {
				return 1;
			}
			adj[r] = -1;
			col[i] = 0;
			dig1[r + i] = 0;
			dig2[r - i + n] = 0;
		}
	}
	return 0;
}
int main() {
	int n;
	cin >> n;
	int ans = nqueen(0, n);
	if(!ans) {
		cout << "No solution" << endl;
	}
	return 0;
}