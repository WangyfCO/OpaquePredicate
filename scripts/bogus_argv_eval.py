# coding=gbk
import angr
import claripy
import sys
import datetime

def main(argv):
  now_start=datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S")
  print('starting!',now_start)
  path_to_binary = argv[1]
  project = angr.Project(path_to_binary)
  
  length=int(argv[2])
  sym_val=claripy.BVS("sym_val",8*length)

  initial_state = project.factory.entry_state(args=[project.filename,sym_val])
  simulation = project.factory.simgr(initial_state)

  def is_successful(state):
    #打印
    print('state:',state)
    stdin_input = state.posix.dumps(sys.stdin.fileno())
    print('stdin_input:',stdin_input)
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    print('stdout_output:',stdout_output)
    #
    return b'Bogus' in stdout_output


  simulation.explore(find=is_successful)
  #打印
  print('simutation:',simulation)

  if simulation.found:
    solution_state = simulation.found[0]

    #打印最终的标准输入输出
    stdin_found =solution_state.posix.dumps(sys.stdin.fileno())
    print('stdin_found:',stdin_found)
    stdout_found =solution_state.posix.dumps(sys.stdout.fileno())
    print('stdout_found:',stdout_found)

    #打印符号变量值
    #无符号整数
    solution=solution_state.solver.eval(sym_val)
    #ASCII码字符串
    solution_bytes=solution_state.solver.eval(sym_val,cast_to=bytes)
    print('Selecting a path to Bogus! Solution is {0}({1})'.format(solution,solution_bytes))

    #打印结束时间
    now_finish=datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    print('finished!',now_finish)
  else:
    now_finish=datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    print('finished!',now_finish)
    raise Exception('Selecting a path to Bogus!Find no solution.')

if __name__ == '__main__':
  main(sys.argv)
