def multiple_size():
  files = glob.glob('data/*')
  for f in files:
      os.remove(f)
  sizes = []
  times = []
  i=50000
  while True:
    i = i*2
    df = read_from_fits("COSMOS_IRAC.fits")
    df = df.random_choise(i).add_noise(param=[0,0.01])
    df.save_as_fits(f"data/IRAC{i}")
    t = time()
    #print(len(sky_irac))
    for j in range(5):
      subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", f"data/IRAC{i}.fits", "0.1",
                    "--out=example1.fits", "--radius", "10", "--prior-completeness", "0.9"])
    print(i)
    print(time()-t)
    times.append((time()-t)/5)
    sizes.append(i)
    if i>50000000:
      break
  import matplotlib.pyplot as plt
  plt.plot(sizes,times)
  plt.xscale("log")
  plt.yscale("log")
  return sizes,times

def multiple_rad():
  files = glob.glob('data/*')
  for f in files:
    os.remove(f)
  j = 10
  times = []
  rows = []
  sizes = []
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(1000000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC1")
  for i in range(5):

    t = time()
    for k in range(1):
      subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                    f"--out=data/example{i}.fits", "--radius", str(j), "--prior-completeness", "0.9"])
    times.append((time()-t)/5)
    print(time()-t)
    df = read_from_fits(f"data/example{i}.fits","XMM_DEC","XMM_RA")
    rows.append(len(df))
    sizes.append(j)
    print(i)
    j*=2
  fig,ax = plt.subplots(1,2)
  fig.tight_layout()
  ax[0].plot(sizes,times)
  ax[1].plot(sizes,rows)
  ax[0].set_xscale("log")
  ax[0].set_yscale("log")
  ax[0].set_title("Время работы")
  ax[0].set_xlabel("Радиус")
  ax[0].set_ylabel("Время (с)")
  ax[1].set_xscale("log")
  ax[1].set_yscale("log")
  ax[1].set_xlabel("Радиус")
  ax[1].set_ylabel("Строки")
  ax[1].set_title("Количество строк")
  return sizes,times,rows
l = multiple_rad();

def multiple_levels():
  files = glob.glob('data/*')
  for f in files:
    os.remove(f)
  t = time()
  times = []
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC1")
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "--out=data/example0.fits", "--radius", "10"])
  times.append(time()-t)
  
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC2")
  t = time()
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "data/IRAC2.fits", "0.1",
                  "--out=data/example1.fits", "--radius", "10"])
  times.append(time()-t)
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC3")
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC4")
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC5")
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC6")
  df = read_from_fits("COSMOS_IRAC.fits")
  df = df.random_choise(100000).add_noise(param=[0,0.01])
  df.save_as_fits(f"data/IRAC7")
  t = time()
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "data/IRAC2.fits", "0.1","data/IRAC3.fits", "0.1",
                  "--out=data/example1.fits", "--radius", "10"])
  times.append(time()-t)
  t = time()
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "data/IRAC2.fits", "0.1","data/IRAC3.fits", "0.1","data/IRAC4.fits", "0.1",
                  "--out=data/example1.fits", "--radius", "10"])
  times.append(time()-t)
  t = time()
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "data/IRAC2.fits", "0.1","data/IRAC3.fits", "0.1","data/IRAC4.fits", "0.1", "data/IRAC5.fits", "0.1",
                  "--out=data/example1.fits", "--radius", "10"])
  times.append(time()-t)
  t = time()
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "data/IRAC2.fits", "0.1","data/IRAC3.fits", "0.1","data/IRAC4.fits", "0.1", "data/IRAC5.fits", "0.1",
                  "data/IRAC6.fits", "0.1",
                  "--out=data/example1.fits", "--radius", "10"])
  times.append(time()-t)
  t = time()
  subprocess.run(["python", "nway.py", "COSMOS_XMM.fits", ":pos_err", "data/IRAC1.fits", "0.1",
                  "data/IRAC2.fits", "0.1","data/IRAC3.fits", "0.1","data/IRAC4.fits", "0.1", "data/IRAC5.fits", "0.1",
                  "data/IRAC6.fits", "0.1", "data/IRAC7.fits", "0.1",
                  "--out=data/example1.fits", "--radius", "10"])
  times.append(time()-t)
  return times
tim = multiple_levels()
