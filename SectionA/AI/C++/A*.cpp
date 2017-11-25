#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ss second
#define ff first
using namespace std;
typedef pair<int, int> ipair;
int n;
int adj[30][30];
int h[30];
int par[30];
vector<string> s;

void initialize() {
	int i, j;
	for(i = 0; i < n; i++) {
		par[i] = -1;
		h[i] = 0;
		for(j = 0; j < n; j++) {
			adj[i][j] = 0;
		}
	}
	string temp[] = { "Arad", "Oradea", "Zerind","Sibiu", "Timisoara", "Lugoj", "Mehadia", "Dobreta", "Craiova", "Rimnicu Vilcea", "Pitesti", "Fagaras", "Giurgiu", "Urziceni", "Eforie", "Hirsova", "Vaslui", "Iasi", "Neamt", "Bucharest"};
	for(i = 0; i < n; i++) {
		s.pb(temp[i]);
	}
}

int findId(string s1) {
	int i;
	for(i = 0; i < n; i++) {
		if(s[i] == s1) {
			return i;
		}
	}
	return -1;
}

void fill1(string s1, string s2, int val) {
	int id1 = findId(s1);
	int id2 = findId(s2);
	if(id1 != -1 || id2 != -1) {
		adj[id1][id2] = val;
		adj[id2][id1] = val;
	}
	else {
		cout << "Invalid name" << endl;
	}
}

void initializeGraph() {
	fill1("Oradea", "Zerind", 71);
	fill1("Oradea", "Sibiu", 151);
	fill1("Zerind", "Arad", 75);
	fill1("Arad", "Sibiu", 140);
	fill1("Arad", "Timisoara", 118);
	fill1("Timisoara", "Lugoj", 111);
	fill1("Lugoj", "Mehadia", 70);
	fill1("Mehadia", "Dobreta", 75);
	fill1("Dobreta", "Craiova", 120);
	fill1("Sibiu", "Fagaras", 99);
	fill1("Sibiu", "Rimnicu Vilcea", 80);
	fill1("Rimnicu Vilcea", "Craiova", 146);
	fill1("Rimnicu Vilcea", "Pitesti", 97);
	fill1("Pitesti", "Bucharest", 101);
	fill1("Fagaras", "Bucharest", 211);
	fill1("Bucharest", "Giurgiu", 90);
	fill1("Urziceni", "Bucharest", 85);
	fill1("Vaslui", "Urziceni", 142);
	fill1("Iasi", "Vaslui", 92);
	fill1("Neamt", "Iasi", 87);
	fill1("Urziceni", "Hirsova", 98);
	fill1("Hirsova", "Eforie", 86);
}

void mark(string s1, int val) {
	int id = findId(s1);
	if(id != -1) {
		h[id] = val;
	}
}

void initializeHeuristics() {
	mark("Arad", 366);
	mark("Bucharest", 0);
	mark("Craiova", 160);
	mark("Dobreta", 242);
	mark("Eforie", 161);
	mark("Fagaras", 176);
	mark("Giurgiu", 77);
	mark("Hirsova", 151);
	mark("Iasi", 226);
	mark("Lugoj", 244);
	mark("Mehadia", 241);
	mark("Neamt", 234);
	mark("Oradea", 380);
	mark("Pitesti", 100);
	mark("Rimnicu Vilcea", 193);
	mark("Sibiu", 253);
	mark("Timisoara", 329);
	mark("Urziceni", 80);
	mark("Vaslui", 199);
	mark("Zerind", 374);
}

void printData() {
	int i, j;
	cout << "Heuristics";
	for(i = 0; i < n; i++) {
		cout << s[i] << " " << h[i] << endl;
	}
	cout << endl;
	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++) {
			cout << adj[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int calcDistance(int src, int dest) {

	priority_queue<ipair, vector<ipair>, greater<ipair> > pq;
	int dist[n];
	int i;
	for(i = 0; i < n; i++) {
		dist[i] = 10000000;
	}
	dist[src] = 0;
	pq.push(mp(dist[src] + h[src], src));
	while(!pq.empty()) {
		ipair p = pq.top();
		pq.pop();
		int id = p.ss;
		dist[id] = p.ff - h[id];
		if(id == dest) {
			break;
		}
		int i;
		for(i = 0; i < n; i++) {
			int k = adj[id][i];
			if(k) {
				if(dist[id] + k < dist[i]) {
					par[i] = id;
					dist[i] = dist[id] + k;
					pq.push(mp(dist[i] + h[i], i));
				}
			}
		}
	}
	return dist[dest];
}

int main() {
	n = 20;
	initialize();
	initializeGraph();
	initializeHeuristics();
	printData();
	int ans = calcDistance(0, n - 1);
	cout << ans << endl;
	return 0;
}