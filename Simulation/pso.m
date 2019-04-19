clc;
clear;
close all;

%% Problem Definition
cost = @(x,a) spot(x,a);

nVar=2;     %dimensions
VarSize=[1 nVar]; 

a=[4,6];

VarMin=-10;
VarMax=10;

%% Parameters
MaxIt=500; %max iterations
nPop=3;
w=0.3;
wdamp=1;
c1=1.5;
c2=1.5;
MaxVel=0.2*(VarMax-VarMin);
MinVel=-MaxVel;

%% Initialisation
tr = zeros(MaxIt,6);

empty_bot.position=[];
empty_bot.velocity=[];
empty_bot.cost=[];
empty_bot.best.position=[];
empty_bot.best.cost=[];

bot=repmat(empty_bot,nPop,1);

globalbest.cost=inf;
for i=1:nPop
    bot(i).position=unifrnd(VarMin,VarMax,VarSize);
    
    bot(i).velocity=zeros(VarSize);
    
    bot(i).cost=cost(bot(i).position,a);

    bot(i).best.position=bot(i).position;
    bot(i).best.cost=bot(i).cost;
    
    if bot(i).best.cost<globalbest.cost
        globalbest=bot(i).best;
    end 
end

bestcosts=zeros(MaxIt,1);
bestpos=zeros(1,nVar);

%% Main
for it=1:MaxIt
    for i=1:nPop
        
        bot(i).velocity = w*bot(i).velocity + c1*rand(VarSize).*(bot(i).best.position-bot(i).position) + c2*rand(VarSize).*(globalbest.position-bot(i).position);
        
        bot(i).velocity=max(MinVel,bot(i).velocity);
        bot(i).velocity=min(MaxVel,bot(i).velocity);
        
        bot(i).position = bot(i).position + bot(i).velocity;
        
        bot(i).position=max(VarMin,bot(i).position);
        bot(i).position=min(VarMax,bot(i).position);
        
            
        bot(i).cost = cost(bot(i).position,a);

        if bot(i).cost<bot(i).best.cost
            bot(i).best.cost=bot(i).cost;
            bot(i).best.position=bot(i).position;
            
            if bot(i).best.cost<globalbest.cost
                
                globalbest=bot(i).best;
            end
        end
    
        
    end
    tr(it,1) = bot(1).position(1);
    tr(it,2) = bot(1).position(2);
    tr(it,3) = bot(2).position(1);
    tr(it,4) = bot(2).position(2);
    tr(it,5) = bot(3).position(1);
    tr(it,6) = bot(3).position(2);
    bestcosts(it)=globalbest.cost;
    bestpos=globalbest.position;
    disp(['It ' num2str(it) ': Best Cost = ' num2str(bestcosts(it))]);
    disp([' Best Position = ' num2str(bestpos)]);
    w=w*wdamp;
    
end

%% Results
%figure;
TR=transpose(tr);
plot(TR(1,:),TR(2,:),'b','LineWidth',2);
hold on;
plot(TR(3,:),TR(4,:),'g','LineWidth',2);
hold on;
plot(TR(5,:),TR(6,:),'r','LineWidth',2);
hold off;
plot(bestcosts,'LineWidth',2);
xlabel('Iterations');
ylabel('Best Cost');
%grid on;
