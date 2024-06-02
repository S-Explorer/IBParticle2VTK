# IBParticle2VTK

<a href="https://github.com/AMReX-Codes/amrex"><img src=https://img.shields.io/badge/amrex-IAMR-pink></a>  <a href="https://github.com/ruohai0925/IAMR/tree/development"><img src=https://img.shields.io/badge/IBM-Particle-blue></a>

---

## introduction

<p><img align="right" src="./docs/Particle2VTK.png" height=600/><font size=6>
We have developed a comprehensive particle resolution calculation program <a href="https://github.com/ruohai0925/IAMR/tree/development">[IB_Particle]</a>, in which particle information is outputted to the case folder, with each particle having its own infomation file. With the tool provided here, these particle information files can be converted into VTK files for visualization using ParaView. 
</p>

## how to use

### 1. generate track

```shell
# python_executable *.py Particle_csv_file
python ParticlePath.py IB_particle_1.csv
#generate IB_particle_1.vtk, all the location with points
```

### 2.generate particle

```shell
# python_executable *.py Particle_csv_file_part time_step 
python ParticlesTimeStep.py IB_particle 100
#generate Particle[time].vtk, all the particle infomation at same time
```

### 3.Read Log info

```shell
# python_executable *.py logFile
python parseLogInfo.py log
#generate TimeStepLevel's cell, max uvw, coarse time
```

