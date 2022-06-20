## SUPERCLASS
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

## GOBLIN CLASS
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line
    
  @desc.setter
  def desc(self, value):
    self._desc = value

## HUMAN CLASS
class Human(GameObject):
  def __init__(self, name):
    self.class_name = "human"
    self._desc = "Just a regular human person like you"
    super().__init__(name)
    
  @property
  def desc(self):
    return self._desc
  
  @desc.setter
  def desc(self, value):
    self._desc = value

## ORC CLASS
class Orc(GameObject):
  def __init__(self, name):
    self.class_name = "orc"
    self.health = 5
    self._desc = " A powerful evil creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >= 5:
      return self._desc
    elif self.health == 4:
      health_line = "Not even a scratch."
    elif self.health == 3:
      health_line = "You have broken its shield."
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

## Input function to interpret the list of commands
def get_input():
  user_input = ""
  while 1:
    try:
      user_input = user_input + input() + "\n"
    except:
      break
  default_input = "say hi\n examine goblin\n question goblin\n hit goblin\n examine goblin\n hit goblin\n examine goblin\n hit goblin\n examine goblin\n examine orc\n question orc\n hit orc\n examine orc\n examine human\n question human\n hit human\n examine human"
  text = user_input if user_input != "\n" else default_input
  comm_list = text.splitlines()
  i = 0
  for line in comm_list:
    command = line.split()
    if len(command) == 1:
      command.append("nothing")
    verb_word = command[0]
    i = i + 1
    print (i,".","You",command[0],command[1])
    if verb_word in verb_dict:
      verb = verb_dict[verb_word]
    else:
      print("Unknown verb {}". format(verb_word))
      return

    if len(command) >= 2:
      noun_word = command[1]
      print (verb(noun_word))
    else:
      print(verb("nothing"))

## Function to react to 'say'
def say(noun):
  return 'You said "{}"'.format(noun)

## Function to react to 'examine'
def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

## Function to react to 'hit'
def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed this servant of evil!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
    elif type(thing) == Orc:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed this servant of evil!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
    elif type(thing) == Human:
      thing.desc = "You tried hitting this poor person. Now it's mad."
      msg = "Why would you hit a human?"
      
  else:
    msg ="There is no {} here.".format(noun) 
  return msg

## Function to react to 'question'
def question(noun):
  if noun in GameObject.objects:
    creature = GameObject.objects[noun]
    try:
      if creature.health > 0:
        msg = "\"My name is " + creature.name + ".\""
      else:
        msg = "Why questioning the dead..."
    except:
      msg = "\"My name is " + creature.name + ".\""
  else:
    msg ="There is no {} here.".format(noun)
  return msg

# Initialising the program with 1 object per class
goblin = Goblin("Gobbly")
orc = Orc("Orcley")
human = Human("Charles")

verb_dict = {
  "say": say,
  "examine": examine,
  "hit": hit,
  "question": question,
}

get_input()
