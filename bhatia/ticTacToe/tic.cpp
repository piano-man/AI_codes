#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
using namespace std;

struct Move {
	int r, c;
	Move() {
		r = 0;
		c = 0;
	}
	Move(int r1, int c1) {
		r = r1;
		c = c1;
	}
};
char arr[4];
int board[3][3]; // 0-> blank, 1->X, 2->O

int player;
int opponent;

void printBoard() {
	int i, j;
	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++) {
			cout << arr[board[i][j]] << " ";
		}
		cout << endl;
	}
}
int isMoveLeft() {
	int i, j;
	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++) {
			if(!board[i][j]) {
				return 1;
			}
		}
	}
	return 0;
}

int evaluate() {
	int i, j;
	//checkRows
	for(i = 0; i < 3; i++) {
		if(board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
			if(board[i][0] == player) {
				return 10;
			}
			else if(board[i][0] == opponent) {
				return -10;
			}
		}
	}

	//checkColumns
	for(i = 0; i < 3; i++) {
		if(board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
			if(board[0][i] == player) {
				return 10;
			}
			else if(board[0][i] == opponent) {
				return -10;
			}
		}
	}
	//Diagonal1
	if(board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
		if(board[0][0] == player) {
			return 10;
		}
		else if(board[0][0] == opponent) {
			return -10;
		}
	}

	//Diagonal2
	if(board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
		if(board[0][2] == player) {
			return 10;
		}
		else if(board[0][2] == opponent) {
			return -10;
		}
	}
	return 0;
}
int minimax(int d, bool isMax) {
	int score = evaluate();
	if(score) {
		return score;
	}
	if(!isMoveLeft()) {
		return 0;
	}
	int i, j;
	if(isMax) {
		int best = -1000;
		for(i = 0; i < 3; i++) {
			for(j = 0; j < 3; j++) {
				if(!board[i][j]) {
					board[i][j] = player;
					best = max(best, minimax(d + 1, !isMax));
					board[i][j] = 0;
				}
			}
		}
		return best;
	}
	else {
		int best = 1000;
		for(i = 0; i < 3; i++) {
			for(j = 0; j < 3; j++) {
				if(!board[i][j]) {
					board[i][j] = opponent;
					best = min(best, minimax(d + 1, !isMax));
					board[i][j] = 0;
				}
			}
		}
		return best;
	}
}

Move findBestMove() {
	int best = -1000;
	Move bestMove(-1, -1);
	int i, j;
	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++) {
			if(!board[i][j]) {
				board[i][j] = player;
				int val = minimax(0, false);
				board[i][j] = 0;
				if(val > best) {
					bestMove.r = i;
					bestMove.c = j;
					best = val;
				}
			}
		}
	}
	return bestMove;
}

int main() {

	arr[0] = '_';
	arr[1] = 'X';
	arr[2] = 'O';
	int i, j;
	char ch;
	string str;
	for(i = 0; i < 3; i++) {
		cin >> str;
		for(j = 0; j < 3; j++) {
			ch = str[j];
			if(ch == 'X') {
				board[i][j] = 1;
			}
			else if(ch == 'O') {
				board[i][j] = 2;
			}
			else {
				board[i][j] = 0;
			}
		}
	}
	cin >> ch;
	if(ch == 'X') {
		player = 2;
		opponent = 1;
	}
	else {
		player = 1;
		opponent = 2;
	}
	int c = 1;
	int f = 1;
	while(isMoveLeft) {
		printBoard();
		if(c) {
			int x, y;
			cin >> x >> y;
			board[x][y] = opponent;
		}
		else {
			Move bestMove = findBestMove();
			cout << "Best Move " << bestMove.r << " " << bestMove.c << endl;
			board[bestMove.r][bestMove.c] = player;
		}
		int k = evaluate();
		if(k == 10) {
			cout << "computer wins\n";
			f = 0;
		}
		else if(k == -10) {
			cout << "player wins\n";
			f = 0;
		}
		printBoard();
		if(!f) {
			break;
		}
		c^=1;
	}
	if(f) {
		cout << "Draw\n";
	}
	return 0;
}