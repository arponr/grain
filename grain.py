import sys, os

basePath = '/Users/arpon/Documents/grain'
nodePath = basePath + '/nodes'
edgePath = basePath + '/edges'
tagPath  = basePath + '/tags'
bashPath = basePath + '/bashout.sh'

bash = []

def invalid(msg):
    print 'invalid: {}'.format(msg)
    sys.exit()

def bashOut():
    with open(bashPath, 'w') as bashf:
        bashf.write('#!/bin/bash\n\n')
        for b in bash:
            bashf.write('{}\n'.format(b))

def node(n):
    ndir = '{}/{}'.format(nodePath, n)
    if not os.path.exists(ndir):
        os.makedirs(ndir)
    bash.append('cd {}'.format(ndir))

def edge(ns):
    ns.sort()
    e = '--'.join(ns)
    edir = '{}/{}'.format(edgePath, e)
    if not os.path.exists(edir):
        os.makedirs(edir)
    bash.append('cd {}'.format(edir))

def tag(n, ts):
    ndir = '{}/{}'.format(nodePath, n)
    if not os.path.exists(ndir):
        invalid('node does not exist')
    with open('{}/tags'.format(ndir), 'a') as nf:
        for t in ts:
            nf.write('{}\n'.format(t))
            with open('{}/{}'.format(tagPath, t), 'a') as tf:
                tf.write('{}\n'.format(n))
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        invalid('argument format')
    cmd = sys.argv[1]
    if cmd == 'node':
        if len(sys.argv) != 3:
            invalid('argument format')
        node(sys.argv[2])
    elif cmd == 'edge':
        if len(sys.argv) < 4:
            invalid('argument format')
        edge(sys.argv[2:])
    elif cmd == 'tag':
        if len(sys.argv) < 4:
            invalid('argument format')
        tag(sys.argv[2], sys.argv[3:])

    bashOut()
