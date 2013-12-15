//testList
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


int main(){

   list<int> al;
   list<int> av;
   for (int i=0;i<10;i++) {
      al.push_back(i);
      av.push_back(i+100);
   }
   
   
   insertAfter(5,al, av);
   
   for (list<int>::iterator it = al.begin(); it != al.end(); it++)  
       cout << *it << " ";
   
   cout << endl;    
   
   return 0;   



}
