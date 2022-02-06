"""
Madlibs generator is a fun game that is usually played by kids.
In this python game user has to enter substitutes for blanks in
the story without knowing the story. It will be fun to read aloud
the stories after filling the blanks.

Here we will discuss 3 ways to code madlibs generator
"""
# ----- Way-1 (Basic method)-------------------------------------------------------------------------------------------------------------
"""
Noun = "bed"
Plural_Noun = "button"
Verb1 = "kill"
Verb2 = "be"
part_of_body ="black"
adj = "open"
Noun1 ="clothes"

print("Today, every student has a computer small enough to fit into his "+Noun)
print("He can solve any math problem by simply pushing the computer's little "+Plural_Noun)
print("Computers can add,multiply,divide , and "+Verb1)
print("They can also "+Verb2+" better than a human.")
print("Some computers are "+part_of_body)
print("Others have a/an "+adj+" screen that shows all kinds of "+Noun1+" and "+" even "+" figures")

"""

# ----- Way-2 (Using format()) --------------------------------------------------------------------------------------------

"""

Noun = "bed"
Plural_Noun = "button"
Verb1 = "kill"

print("Today, every student has a computer small enough to fit into his {} ".format(Noun))
print("He can solve any math problem by simply pushing the computer's little {} ".format(Plural_Noun))


"""

# -----  way-3 (Using F string)-----------------------------------------------------------------------------------------------------------


Noun = input("Noun\t")
Plural_Noun = input("Plural Noun\t")
Verb1 = input("Verb1\t")
Verb2 = input("Verb2\t")
part_of_body =input("part_of_body\t")
adj = input("Adjective\t")
Noun1 =input("Noun1\t")

print(f"Today, every student has a computer small enough to fit into his {Noun}")
print(f"He can solve any math problem by simply pushing the computer's little {Plural_Noun}")
print(f"Computers can add ,multiply,divide , and {Verb1}")
print(f"They can also {Verb2} better than a human.")
print(f"Some computers are {part_of_body}")
print(f"Others have a/an {adj} screen that shows all kinds of {Noun1} and  even  figures")
