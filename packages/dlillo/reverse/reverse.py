def reverse(args):
  inp = args.get("input","")
  out = "dammi un input che te lo rivolto io"
  if inp != "":
    out = "L'input al contrario è: **" + inp[::-1] + "**" 
    
  return { "output": out }
