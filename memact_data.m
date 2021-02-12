function [memact] = memact_data(pacientid,RT_corr, U1,U2,tabs,eegfile)
% memact_data creates and returns the structure with events in MemoryActions test 
% pacientid - id pacienta, napriklad p85, podle pojmenovani vystupni tabulky
% U1 a U2 vystup z udalosti2() - casy synchropulsu k podnedu a odpovedi

if ~exist('RT_cor','var')  || isempty(RT_cor)
    RT_corr = 0; % default: RT of start moving joystick, if 1 - RT of hiting the correct object 
end

dir = 'e:\работа\MemoryActions\data\';
% load mat file with all behav data
load([dir pacientid '_MemoryActions.mat']);

% get only table with RT, accuracy and so on, without coordinates of joystick 
dataS = MemoryActions.Gdata;

% rearrange data according to Kamil's format
data(:,1) = dataS(:,7);  % instead of soubor - delay
data(:,2) = dataS(:,9); % answer_button (to the question in diff conditions)
data(:,3) = dataS(:,4); % spravne = accuracy
if RT_corr == 0
    data(:,4) = dataS(:,6); % rt of start
else
    data(:,4) = dataS(:,5); % rt of correct
end
data(:,5) = dataS(:,3); % opakovani = block
data(:,6) = dataS(:,2); % feedback = zpetnavazba
data(:,7) = dataS(:,1); % condition = kategorie

if size(U1,1) ~= size(data,1) || size(U2,1) ~= size(data,1)
    disp(['data:' num2str(size(data,1)) ' U1:' num2str(size(U1,1)) ' U2:' num2str(size(U2,1))]);
    error('different lengths of data and events, cannot be processed!');    
end

data(:,8)=U1(:,2);
data(:,9)=U2(:,2);

%nazvy sloupcu tabulky
sloupce = {};
sloupce.delay=1;   % instead of soubor - time of delay in delayed conditions
sloupce.klavesa=2; % answer_button response (to the question in diff conditions)
sloupce.spravne=3;
sloupce.rt = 4;
sloupce.opakovani=5;
sloupce.zpetnavazba=6;
sloupce.kategorie=7;
sloupce.ts_podnet=8;
sloupce.ts_odpoved=9;

%retezcove hodnoty kodu klavesa a faktoru testu
klavesa = cell(3,2);
klavesa(1,:)={'incorrect' 0};
klavesa(2,:)={'correct' 1};
klavesa(3,:)={'none' NaN};

podminka = cell(4,2);
podminka(1,:)={'immed_same' 0};
podminka(2,:)={'immed_diff' 1};
podminka(3,:)={'del_same' 2};
podminka(4,:)={'del_diff' 3};

memact = struct('data',data,'sloupce',sloupce);
memact.strings.klavesa = klavesa;
memact.strings.podminka = podminka; %kategorie, aby nazev byl stejny jako u PPA

%timestampy zacatku a konce dat z testu
memact.interval = [tabs(1) tabs(end)];
disp(['MemActions data od ' datestr(tabs(1),'dd-mmm-yyyy HH:MM:SS.FFF') ' do ' datestr(tabs(end),'dd-mmm-yyyy HH:MM:SS.FFF')]);

memact.eegfile = eegfile;
memact.pacientid = pacientid; %6.6.2018 - proc jsem to tam probuh nemel driv?
end

