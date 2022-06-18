from flask import Flask, render_template, redirect
from mem import create_memes

app = Flask(__name__)
luck = 1
tim = 0
arr_mem = create_memes()
counter = 200
best_mem = max(arr_mem, key=lambda x: x[1])

@app.route('/')
def greeting():
  return redirect("/0/")
  


@app.route('/<int:a>/')
def index(a):
  global arr_mem, counter, luck, tim
  arr_mem[tim][1] += a
  
  counter = counter % 1200 + 1

  luck = (luck + 1) % 2
  
  if (luck):
    tim = 5
    return render_template('main.html', link=arr_mem[5][0], number=arr_mem[5][1])
    
  while( (best_mem[1] - arr_mem[counter][1]) < 2 ):
    counter = counter % 52 + 1

  tim = counter
  return render_template('main.html', link=arr_mem[counter][0], number=arr_mem[counter][1])




@app.route('/best/')
def best():
  global best_mem
  best_mem = max(arr_mem, key=lambda x: x[1])
  
  return render_template('best.html', link=best_mem[0], number=best_mem[1])

app.run(host='0.0.0.0', port=81)
