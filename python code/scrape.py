from wsgiref import headers
import requests
import pandas as pd


#change season id! to get the stats u want :) 
season_id = '2020-21'
per_mode = 'Totals'

team_info_url = 'https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+per_mode+'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+season_id+'&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='

headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

response = requests.get(url=team_info_url, headers=headers).json()

team_info = response['resultSets'][0]['rowSet']
#print(team_info)

#was unsure of which columns I wanted intially so I took all - cleaned later in python using jupyter notebook

#column names, headers from prev results
columns_list = [
'team_id',
'team_name',
'gp',
'w',
'l',
'w_pct',
'min',
'fgm',
'fga',
'fg_pct',
'fg3m',
'fg3a',
'fg3_pct',
'ftm',
'fta',
'ft_pct',
'oreb',
'dreb',
'reb',
'ast',
'tov',
'stl',
'blk',
'blka',
'pf',
'pfd',
'pts',
'plus_minus',
'gp_rank',
'w_rank',
'l_rank',
'w_pct_rank',
'min_rank',
'fgm_rank',
'fga_rank',
'fg_pct_rank',
'fg3m_rank',
'fg3a_rank',
'fg3_pct_rank',
'ftm_rank',
'fta_rank',
'ft_pct_rank',
'oreb_rank',
'dreb_rank',
'reb_rank',
'ast_rank',
'tov_rank',
'stl_rank',
'blk_rank',
'blka_rank',
'pf_rank',
'pfd_rank',
'pts_rank',
'plus_minus_rank',
'cfid',
'cfparams'
]

nba1_df = pd.DataFrame(team_info, columns = columns_list)

#seeing what i've got!
print(nba1_df.sample(6))

#saving file to desktop

nba1_df.to_csv(r'C:\\desktop\\team_2020-21.csv', index=False)
