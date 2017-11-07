#include<iostream>
#include<map>
#include<stack>
#include<vector>
#include<queue>
#include<algorithm>
#define vvi vector<vector<int> >
 
using namespace std;
 
void rotate_row(vvi &v,int row)
{
	int n=v.size();
	int temp=v[row][n-1];
	for(int i=n-2;i>=0;i--)
	{
		v[row][i+1]=v[row][i];
	}
	v[row][0]=temp;
}
 
void rotate_column(vvi &v,int column)
{
	int n=v.size();
	int temp=v[n-1][column];
	for(int i=n-2;i>=0;i--)
	{
		v[i+1][column]=v[i][column];
	}
	v[0][column]=temp;
}
 
void print_matrix(stack<vvi> &s)
{
 
	int n=s.top().size();
	while(!s.empty())
	{
		vvi v=s.top();
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				cout<<v[i][j]<<" ";
			}
		}
		cout<<endl;
		s.pop();
	}
	//cout<<s.size()<<endl;
}
 
bool DLS(vvi &source,vvi &goal,int limit,stack<vvi> &s)
{
	int n=source.size();
	
		
	if(source==goal){
		s.push(source);
		return true;
	}
	
	if(limit<0)
		return false;
		
	vvi temp=source;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-1;j++)
		{
			rotate_row(source,i);
			if(DLS(source,goal,limit-1,s))
			{
				s.push(temp);
				return true;
			}
		}
		source=temp;
	}
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n-1;j++)
		{
			rotate_column(source,i);
			if(DLS(source,goal,limit-1,s))
			{
				s.push(temp);
				return true;
			}
		}
		source=temp;
	}
	
	return false;
}
void IDDFS(vvi &source,vvi &goal)
{
	stack<vvi> s;
	for(int i=0;i<100;i++)
	{
		cout << i << endl;
		if(DLS(source,goal,i,s))
		{ 
			print_matrix(s); 
			return;
		}
	}
}
 
int main()
{
	int t,m,n,temp;
	cin>>t;
	while(t--)
	{
		cin>>n;
		vvi source(n),goal(n);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				cin>>temp;
				source[i].push_back(temp);
			}
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				cin>>temp;
				goal[i].push_back(temp);
			}
		}
		IDDFS(source,goal);
	}
	
	return 0;
}