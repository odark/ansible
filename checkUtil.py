#!/usr/bin/python
import os

def getForks():
  thread = input('Thread Count (Enter: default=1) : ');
  if thread == '':
    thread = '1'
  return thread
