from random import randint

name = raw_input('enter your name:')

try:
    f = open('game.txt','r')
except:
    f = file('game.txt','w')
    f = open('game.txt','w')
    f.write('0 0 0')
    f = open('game.txt','r')
    
#score = f.read().split()
#game_times = int(score[0])
#min_times = int(score[1])
#total_times = int(score[2])

lines = f.readlines()
f.close()

scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
    
score = scores.get(name)
print(score)

if score is None:
    score = [0,0,0]
    
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times > 0:
        avg_times = float(total_times) / game_times
else:
    avg_times = 0

print 'You have Played %d times,guessed the answer use %d time for the least times,%d times is average'% (game_times, min_times, avg_times)

num = randint(1,100)
times = 0
print 'Guess what I think?'
bingo = False

while bingo == False:
    times +=1
    answer = input()

    if answer < num:
        print 'too small!'

    if answer > num:
        print 'too big!'

    if answer == num:
        print 'Bingo!'
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times

total_times += times
game_times += 1

scores[name] = [str(game_times),str(min_times),str(total_times)]
result = ''

for n in scores:
    print(n)
    line = n + ' ' + ' '.join(scores[n])+'\n'
    result += line

f = open('game.txt', 'w')
f.write(result)
f.close()
