#MadLib.py
#Name:Emma Barnes
#Date:01/22/2026
#Assignment: MadLib - Lab 01

def main():
  print("Madlib")
  #Ask user for words
  number = input("Give me a number 1-12: ")
  adv1 = input("Give me an adverb: ")
  adj1 = input ("Give me an adjective: ")
  animal = input ("Give me an animal: ")
  adj2 = input ("Give me another adjective: ")
  article_of_clothing = input ("Give me an article of clothing: ")
  ocean = input("Give me the name of an ocean: ")
  adv2 = input("Give me an -ly adverb: ")
  adj3 = input("Give me an adjective: ")
  body_part = input("Give me the name of a body part: ")
  adj4 = input("Give me another adjective: ")

  #Print the story with the user supplied words.
  print(f"This morning my alarm went off {adv1} at {number} AM. I was in the middle of a {adj1} dream! I was riding a/an {animal} in my {adj2} {article_of_clothing}, on a remote island in the {ocean} ocean. I thought the ringing of my alarm was the sound of a {adj3} ship coming to rescue me! When I {adv2} realized it was my alarm, I sat up so fast I bumped my {body_part} on my nightstand. That’s the {adj4} story of my morning.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
