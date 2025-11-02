//
// Created by Abraham on 2025/5/26.
//
#include<iostream>
#include<algorithm>
#include <set>
#include<cstring>
#include "queue"

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define MAX int(1005)
#define INF ll(1e64)
set<ll> S;
int aim[4][4],aimx[9],aimy[9],Hashpow[9];
struct state{
    int cur[4][4];
    ll hash;
    int id,pre;
    int p,d;
    int x0,y0;
    state(){
        memset(cur,0, sizeof(cur));
    }
    friend bool operator < (const state &a,const state &b){
        return a.p>b.p;
    }
};
vector<state> states;
priority_queue<state>pri;
ll Hash(state &a){
    ll r=0;
    for(int i=1;i<4;i++){
        for(int j=1;j<4;j++){
            r+=Hashpow[3*(i-1)+j]*a.cur[i][j];
        }
    }
    return r;
}
state copy(state &a){
    state b=state();
    b.pre=a.id;
    b.d=a.d+1;
    b.x0=a.x0;
    b.y0=a.y0;
    for(int i=1;i<4;i++){
        for(int j=1;j<4;j++){
            b.cur[i][j]=a.cur[i][j];
        }
    }
    return b;
}
inline int mhd(int x,int y,int i,int j){
    return abs(x-i)+abs(y-j);
}
inline int h(int a[4][4]){
    int r=0;
    for(int i=1;i<4;i++){
        for(int j=1;j<4;j++){
            r+=mhd(i,j,aimx[a[i][j]],aimy[a[i][j]]);
        }
    }
    return r;
}
void move(state &a,int xc,int yc){
    swap(a.cur[a.x0][a.y0],a.cur[a.x0+xc][a.y0+yc]);
    a.x0+=xc;
    a.y0+=yc;
    a.p=a.d+h(a.cur);
    a.hash= Hash(a);
}
state Astar(state &s){
    int index=0;
    states.push_back(s);
    int x0=states[index].x0;
    int y0=states[index].y0;
    state tmp=states[0];
    while(tmp.p!=tmp.d){
        if(x0<3){
            state b= copy(tmp);
            move(b,1,0);
            if(!S.count(b.hash)) {
                S.insert(b.hash);
                states.push_back(b);
                b.id=++index;
                pri.push(b);
            }
        }
        if(x0>1){
            state b= copy(tmp);
            move(b,-1,0);
            if(!S.count(b.hash)) {
                S.insert(b.hash);
                states.push_back(b);
                b.id=++index;
                pri.push(b);
            }
        }
        if(y0>1){
            state b= copy(tmp);
            move(b,0,-1);
            if(!S.count(b.hash)) {
                S.insert(b.hash);
                states.push_back(b);
                b.id=++index;
                pri.push(b);
            }
        }
        if(y0<3){
            state b= copy(tmp);
            move(b,0,1);
            if(!S.count(b.hash)) {
                S.insert(b.hash);
                states.push_back(b);
                b.id=++index;
                pri.push(b);
            }
        }
        if(!pri.empty()) {
            tmp=pri.top();
            pri.pop();
        }
        else break;
        x0=tmp.x0;
        y0=tmp.y0;
    }
    return tmp;
}
void show(state &a){
    if(a.pre!=-1){
        show(states[a.pre]);
    }
    for(int i=1;i<4;i++){
        for(int j=1;j<4;j++){
            cout<<a.cur[i][j]<<(j<3?' ':'\n');
        }
    }
    cout<<endl;
}
int main(){
    state be=state();
    for(int i=1;i<4;i++){
        for(int j=1;j<4;j++){
            cin>>be.cur[i][j];
            if(be.cur[i][j]==0){
                be.x0=i;
                be.y0=j;
            }
        }
    }
    be.pre=-1;
    be.id=0;
    be.d=0;
    for(int i=1;i<4;i++){
        for(int j=1;j<4;j++){
            cin>>aim[i][j];
            aimx[aim[i][j]]=i;
            aimy[aim[i][j]]=j;
        }
    }
    Hashpow[0]=1;
    for(int i=1;i<9;i++){
        Hashpow[i]=Hashpow[i-1]*9;
    }
    move(be,0,0);
    state ans=Astar(be);
    cout<<ans.d<<endl;
    show(ans);
    return 0;
}
