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
    #��ӡ
    print('state:',state)
    stdin_input = state.posix.dumps(sys.stdin.fileno())
    print('stdin_input:',stdin_input)
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    print('stdout_output:',stdout_output)
    #
    return b'Foo' in stdout_output


  simulation.explore(find=is_successful)
  #��ӡ
  print('simutation:',simulation)

  if simulation.found:
    solution_state = simulation.found[0]

    #��ӡ���յı�׼�������
    stdin_found =solution_state.posix.dumps(sys.stdin.fileno())
    print('stdin_found:',stdin_found)
    stdout_found =solution_state.posix.dumps(sys.stdout.fileno())
    print('stdout_found:',stdout_found)

    #��ӡ���ű���ֵ
    #�޷�������
    solution=solution_state.solver.eval(sym_val)
    #ASCII���ַ���
    solution_bytes=solution_state.solver.eval(sym_val,cast_to=bytes)
    print('Selecting a path to Foo! Solution is {0}({1})'.format(solution,solution_bytes))

    #��ӡ����ʱ��
    now_finish=datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    print('finished!',now_finish)
  else:
    now_finish=datetime.datetime.now().strftime("%Y-%m-%d %H-%M:%S")
    print('finished!',now_finish)
    raise Exception('Selecting a path to Foo!Find no solution.')

if __name__ == '__main__':
  main(sys.argv)
