import sys
import os
import glob
import pandas as pd

def writeTimeStepFile(time, X, Y, Z, U, V, W, Fx, Fy, Fz):
    with open('IBPartilce' + str(time) + '.vtk','w') as out:
        particleNum = len(X)

        X_m = []
        Y_m = []
        Z_m = []
        U_m = []
        V_m = []
        W_m = []
        Fx_m = []
        Fy_m = []
        Fz_m = []

        for i in range(0, particleNum, 1):
            X_m.append(X[i][time])
            Y_m.append(Y[i][time])
            Z_m.append(Z[i][time])
            U_m.append(U[i][time])
            V_m.append(V[i][time])
            W_m.append(W[i][time])
            Fx_m.append(Fx[i][time])
            Fy_m.append(Fy[i][time])
            Fz_m.append(Fz[i][time])

        out.write('# vtk DataFile Version 4.0\n'
                  'Generated by LXZ-pycode\n'
                  'ASCII\n'
                  'DATASET POLYDATA\n')
        # write location
        out.write('POINTS ' + str(particleNum) + ' double\n')
        for i in range(0, particleNum, 1):
            out.write(str(X_m[i]) + ' ' + str(Y_m[i]) + ' ' + str(Z_m[i]) + '\n')
        # write VERTICES
        out.write('VERTICES ' + str(particleNum) + ' ' + str(particleNum * 2) + '\n')
        for i in range(0, particleNum, 1):
            out.write('1 ' + str(i) + '\n')
        # write velocity data
        out.write('\nPOINT_DATA '+ str(particleNum) + '\nFIELD FieldData 2\n')
        out.write('v 3 ' + str(particleNum) + ' double\n')
        for i in range(0, particleNum, 1):
            out.write(str(U_m[i]) + ' ' + str(V_m[i]) + ' ' + str(W_m[i]) + '\n')
        # write ib force
        out.write('ib_f 3 ' + str(particleNum) + ' double\n')
        for i in range(0, particleNum, 1):
            out.write(str(Fx_m[i]) + ' ' + str(Fy_m[i]) + ' ' + str(Fz_m[i]) + '\n')

        out.close()
        print('generate particle vtk file done , time : ', time)


def doGenerate():
    particleFiles = glob.glob(sys.argv[1]+'*')
    print('detecting exits file : \n')
    for particle in particleFiles:
        print('\t',particle)
        
    result = input('\nis your needed file ?[y/n]')
    result = result.lower()
    if result == 'n':
        print('\nending...\n')
        return

    X = []
    Y = []
    Z = []
    U = []
    V = []
    W = []
    Fx = []
    Fy = []
    Fz = []
    for particle in particleFiles:
        data = pd.read_csv(particle)
        X.append(data['X'])
        Y.append(data['Y'])
        Z.append(data['Z'])
        U.append(data['Vx'])
        V.append(data['Vy'])
        W.append(data['Vz'])
        Fx.append(data['Fx'])
        Fy.append(data['Fy'])
        Fz.append(data['Fz'])

    totSteps = X[0].size

    for i in range(0, totSteps, int(sys.argv[2])):
        writeTimeStepFile(i, X, Y, Z, U, V, W, Fx, Fy, Fz)




if __name__ == '__main__':
    argv1 = sys.argv[1]
    if argv1 == 'help' :
        print('run with Particle IB file name , sunch as :\n\n'
              '/{your python env}/python ParticleTimeStep.py IB_*.csv 10\n\n'
              'will be generate VTK data file , you can open it(*.vtk) with paraview\n'
              '*** but run this file, need pandas to deal data ***\n'
              '*** written by LXZ , 2024/5 ***\n')
        exit()

    doGenerate()