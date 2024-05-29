#!/usr/bin/env python3

class MyString:
  def __init__(self, value="") -> None:
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else:
      self._value = new_value
      
  
  def is_sentence(self):
    return self.value[-1] == "."
  
  def is_question(self):
    return self.value[-1] == "?"
  
  def is_exclamation(self):
    return self.value[-1] == "!"
  
  def count_sentences(self):
    return sum(1 for char in self.value if char == "." or char == "?" or char == "!")