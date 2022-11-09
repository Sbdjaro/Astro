def multiple_size():
  sizes = []
  times = []
  i=50000
  while True:
    i = i*2
    df = read_from_fits("COSMOS_IRAC.fits")
    df = df.random_choise(i).add_noise(param=[0,0.1])
    df.save_as_fits(f"data/IRAC{i}")
    t = time()
    #print(len(sky_irac))
    subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", f"data/IRAC{i}.fits", "0.1",
                    "--out=example1.fits", "--radius", "10", "--prior-completeness", "0.9"])
    print(i)
    print(time()-t)
    times.append(time()-t)
    sizes.append(i)
    if i>50000000:
      break


  import matplotlib.pyplot as plt
  plt.plot(sizes,times)
  plt.xscale("log")
  plt.yscale("log")
  
def multiple_err():
  from time import time
  import subprocess
  j = 1
  mistakes = []
  times = []
  #rows = []
  for i in range(6):
    j*=2
    df = read_from_fits("COSMOS_IRAC.fits")
    df.dataframe["err_ch1"]*=j
    df.save_as_fits(f"data/IRAC{i}")
    t = time()
    subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", f"data/IRAC{i}.fits", "0.1",
                    "--out=example1.fits", "--radius", "10", "--prior-completeness", "0.9"])
    times.append(time()-t)
    mistakes.append(j)
    
  import matplotlib.pyplot as plt
  plt.plot(mistakes,times)
