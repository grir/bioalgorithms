#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <list>
#include <set>
#include <algorithm>
#include <map>
#include <utility> 

using namespace std;

class Edge{
   public:
   int v1;
   int v2; 
   Edge(int s, int t): v1(s), v2(t){};
};

vector< Edge > graph;

//map<int, vector<int> > graph;

/*
bool less (vector<int> v1  ,vector<int> v2) { 

   return ( v1[0]<v2[0] ); 

}

struct lessThan {
  
  bool operator() (vector<int>& v1  ,vector<int>& v2) { 
     return (v1[0]<v2[0]);
  }
  
} obj;
*/
string reduct(string s)
{

   string str = "";
   int ll = s.length();
   for (int i=0; i<ll; i++)
       if ((s[i]=='-') || (s[i]=='>') || (s[i]==','))
           str = str + ' ';
       else
           str = str + s[i];

   return str;

}
//////////////////////////////////////////////////////
void readData(string fname)
{

   ifstream fin( fname.c_str() );
   string line;
   //cout << fname << endl;

   while (getline(fin, line))
   {


       string reds =  reduct(line);

       stringstream ssin(reds);
       int vert, v;
       vector<int> row;
       ssin >> vert;
       while (ssin >> v) {
           Edge edge(vert,v);
        //   Edge edge2(v,vert);
           graph.push_back( edge );
       //    graph.push_back( edge2 );
           
       } 

   }
   
   fin.close();
}
////////////////////////////////////////////////////////////

int findEdgeByV1(int v, bool* used){

    int ll = graph.size();
    for(int i = 0; i < ll; i++)
       if ( (graph[i].v1 == v) && ! used[i])
           return i;
    
    return -1;       

}
////////////////////////////////////////////////////////////
void insertAfter(int findValue, list<int>& base, list<int>& toInsert){

   list<int>::iterator itf;
   bool found = false;
   for (list<int>::iterator it = base.begin(); it != base.end(); it++)  
      if ( *it == findValue ){
         itf = it;
         found = true;
      }   
         
         
   if ( ! found )  return;
   
   
   base.insert(++itf, toInsert.begin(), toInsert.end());    
  
   return;  


}
///////////////////////////////////////////////////////////
list<int> getCycle(int vi, bool* used){
  list<int> path;

  int ll = graph.size();

  int v = graph[vi].v1;
  set<int> trav;
  trav.insert(v);
  
  int nxtv;
  
  path.push_back(v);
  
  int edge = findEdgeByV1(v,used);
  nxtv = graph[edge].v2;
  used[edge] = true;
  
  do {
     trav.insert(nxtv);
     path.push_back(nxtv);  
     edge = findEdgeByV1( nxtv, used );   
     nxtv = graph[edge].v2;
     used[edge] = true;
  } while ( trav.find(nxtv) == trav.end() );

  path.push_back(nxtv);      

  return path;

}
//////////////////////////////////////////////////////

void printList(list<int>& lst){

  for(list<int>::iterator i = lst.begin(); i != lst.end(); i++)
     cout << *i << " ";
  
  cout << endl;

}
///////////////////////////////////////////////////////////////////

list<int> euler(){

  // first cycle
  list<int> path;

  int ll = graph.size();
  bool used[ ll ];
  for (int i=0;i<ll;i++)
     used[i] = false;
  

  int v = 0;//graph[0].v1;
  set<int> trav;
  trav.insert(v);
  
  int nxtv;
  
  path.push_back(v);
  
  int edge = findEdgeByV1(v,used);
  nxtv = graph[edge].v2;
  used[edge] = true;
  
  do {
     trav.insert(nxtv);
     path.push_back(nxtv);  
     edge = findEdgeByV1( nxtv, used );   
     nxtv = graph[edge].v2;
     used[edge] = true;
  } while ( trav.find(nxtv) == trav.end() );


  edge = findEdgeByV1( nxtv, used );   
  nxtv = graph[edge].v2;
  used[edge] = true;
  path.push_back(nxtv);      

  // other cycles:
  
  printList(path);
 /* 
  while (true){
  
     int v = -1;
     for(int i=0;i<ll;i++) 
        if (!used[i]) {
          v=i;
          break;
        }
     if (v == -1) break;
     
     list<int> path1 = getCycle(v, used);
     
     list<int>::iterator it, it1;
      
     for(it=path.begin(); it != path.end(); ++it)
         if ( *it == graph[ v ].v1 ) break;
    // it++; //?    

     printList(path1);
     
     path1.pop_back();
     path1.pop_front();
     
     
     for (it1=path1.begin(); it1 != path1.end(); it1++)
       path.insert(it, *it1);
  
  }
*/

  return path;


}



//////////////////////////////////////////////////////

int main()
{
   readData("input.dat");
   list<int> path = euler();
   printList(path);
   

   return 0;
}
