#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
using namespace std;
typedef pair<int, int> ipair;
typedef pair<int, ipair> tpair;

int adj[300][300];
int col[300];
int edges[300];
int n;
int tColour;
int valid[300];
int vis[300];
vector<tpair> getMRVDH() {
	vector<tpair> v1;
	int i, j;
	for(i = 1; i <= n; i++) {
		if(!col[i]) {
			for(j = 1; j <= tColour; j++) {
				valid[j] = 1;
			}
			for(j = 1; j <= n; j++) {
				if(adj[i][j] && col[j]) {
					valid[col[j]] = 0;
				}
			}
			int c = 0;
			for(j = 1; j <= tColour; j++) {
				if(valid[j]) {
					c++;
				}
			}
			v1.pb(mp(c, mp(-edges[i], i)));
		}
	}
	sort(v1.begin(), v1.end());
	return v1;
}
int getIndividual(int id) {
	int c = 0;
	int i;
	for(i = 1; i <= tColour; i++) {
		vis[i] = 1;
	}
	for(i = 1; i <= n; i++) {
		if(adj[id][i] && col[i]) {
			vis[col[i]] = 0;
		}
	}
	for(i = 1; i <= tColour; i++) {
		c+=vis[i];
	}
	return c;
}
int getTotal(int id) {
	int sum = 0;
	int i;
	for(i = 1; i <= n; i++) {
		if(adj[id][i]) {
			sum+=getIndividual(i);
		}
	}
	return sum;
}

int findColouring(int cnt) {
	if(cnt == n) {
		return 1;
	}
	vector<tpair> ord = getMRVDH();
	int i, j;
	for(i = 0; i < ord.size(); i++) {
		tpair el = ord[i];
		int id = el.ss.ss;
		vector<ipair> ord2;
		for(j = 1; j <= tColour; j++) {
			valid[j] = 1;
		}
		for(j = 1; j <= n; j++) {
			if(adj[id][j] && col[j]) {
				valid[col[j]] = 0;
			}
		}
		for(j = 1; j <= tColour; j++) {
			if(valid[j]) {
				col[id] = j;
				int val = getTotal(id);
				ord2.pb(mp(val, j));
				col[id] = 0;
			}
		}
		sort(ord2.rbegin(), ord2.rend());
		for(j = 0; j < ord2.size(); j++) {
			int sc = ord2[i].ss;
			col[id] = sc;
			if(findColouring(cnt + 1)) {
				return 1;
			}
			col[id] = 0;
		}
	}
	return 0;

}
int main() {

	cin >> n;
	while(1) {
		int a, b;
		cin >> a >> b;
		if(a == -1) {
			break;
		}
		edges[a]++;
		edges[b]++;
		adj[a][b] = adj[b][a] = 1;
	}
	cin >> tColour;
	int i;
	if(findColouring(0)) {
		for(i = 1; i <= n; i++) {
			cout << i << " " << col[i] << endl;
		}
	}
	else {
		cout << "Not Possible\n";
	}
	return 0;
}