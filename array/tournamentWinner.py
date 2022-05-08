'''
My solution
'''
# O(n) time | O(k) where n is the number of competitions
# and k is number of teams


def tournamentWinner(competitions, results):
    # hash set to keep track of scores
    teams = {}
    for i in range(len(competitions)):
        homeTeam = competitions[i][0]
        awayTeam = competitions[i][1]
        # Away team wins
        if results[i] == 0:
            if awayTeam in teams:
                teams[awayTeam] += 3
            else:
                teams[awayTeam] = 3
        # Home team wins
        else:
            if homeTeam in teams:
                teams[homeTeam] += 3
            else:
                teams[homeTeam] = 3

    winner = ""
    maxScore = 0
    # Loop through each team's score and update maxScore
    for team, score in teams.items():
        currentMaxScore = max(maxScore, score)
        if currentMaxScore > maxScore:
            maxScore = currentMaxScore
            winner = team
    return winner


'''
Algoexpert Solution
HOME_TEAM_WON = 1

# O(n) time | O(k) space - where n is the number
# of competitions and k is the number of teams
def tournamentWinner(competitions, results):
	currentBestTeam = ""
	scores = {currentBestTeam: 0}
	
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam, awayTeam = competition
		
		winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
		
		updateScores(winningTeam, 3, scores)
		
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	
	return currentBestTeam

def updateScores(team, points, scores):
	if team not in scores:
		scores[team] = 0
	
	scores[team] += points
'''
