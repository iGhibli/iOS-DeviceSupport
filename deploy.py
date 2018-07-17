#!/usr/bin/env python
import argparse
import zipfile
from os import listdir, path

SRC = path.join(path.dirname(path.abspath(__file__)), 'DeviceSupport')
DEVICE_SUPPORT_PATH='Contents/Developer/Platforms/iPhoneOS.platform/DeviceSupport'

def unzip_file(name, target):
  f = path.join(SRC, name + '.zip')
  zip_ref = zipfile.ZipFile(f, 'r')
  zip_ref.extractall(target)
  zip_ref.close()

def process(xcode):
  target = path.join(xcode, DEVICE_SUPPORT_PATH)
  exist = listdir(target)
  all_files = [i.replace('.zip', '') for i in listdir(SRC) if i.endswith('.zip')]
  new_files = list(set(all_files) - set(exist))
  for i in new_files:
    print 'Unzip file "{}.zip" to {}'.format(i, target)
    unzip_file(i, target)
  print '\nUpdate successfully for {}'.format(xcode)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-t',
    type=str,
    dest='target',
    default='/Applications/Xcode.app',
    help='The path for Xcode'
  )
  args = parser.parse_args()
  process(args.target)
