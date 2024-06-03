import re
import sys

# [Level 1 step 1] Advanced 32768 cells
LevelCells = re.compile(r'\[Level ([0-9]) step (\d+)\] Advanced (\d+) cells')
# max(abs(u/v/w))  = 2.513031039e-08  2.376070415e-08  1.12222
MaxVelocity = re.compile(r'max\(abs\(u/v/w\)\)\s*=\s*(\d\.\d+e?.\d+)\s*(\d\.\d+e?.\d+)\s*(\d\.\d+e?.\d+)\s*')
# [STEP 1] Coarse TimeStep time: 1.714825182
CoarseTime = re.compile(r'\[STEP (\d+)\] Coarse TimeStep time: (\d\.\d+)')

def parseFile():
    filename = sys.argv[1]
    levelCell = open('LevelCell.csv','w')
    MaxU = open('maxVelocity.csv','w')
    TimeSpend = open('TimeSpend.csv','w')
    levelCell.write('step,level,cells\n')
    MaxU.write('step,level,u,v,w\n')
    TimeSpend.write('step,coraseTime\n')
    level = 0
    step = 0
    with open(filename, 'r') as log:
        for line in log:
            cells = LevelCells.findall(line)
            velocity = MaxVelocity.findall(line)
            coarseTime = CoarseTime.findall(line)
            if len(cells) > 0:
                # print(cells)
                print('level:', cells[0][0], ',step:', cells[0][1], ',cells:',cells[0][2])
                level = int(cells[0][0])
                step = int(cells[0][1])
                levelCell.write(cells[0][1]+','+cells[0][0]+','+cells[0][2]+'\n')
            if len(velocity) > 0:
                # print(velocity)
                print('max u v w , u:',velocity[0][0],',v:',velocity[0][1],',w:',velocity[0][2])
                MaxU.write(str(step)+','+str(level)+','+velocity[0][0]+','+velocity[0][1]+','+velocity[0][2]+'\n')
            if len(coarseTime) > 0:
                # print(coarseTime)
                print('STEP:',coarseTime[0][0],',Coarse time:',coarseTime[0][1])
                TimeSpend.write(str(step)+','+coarseTime[0][1]+'\n')
    levelCell.close()
    MaxU.close()
    TimeSpend.close()
            
if __name__ == '__main__':
    parseFile()
