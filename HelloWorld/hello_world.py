print("/n Welcome to the Adventure Program!")
print("/n This is your adventure! Once prompted enter your name to begin your story!")

name = input("Enter your name: /n")
print("Welcome", name)

first = input("You wake up and you've realized that you are in the middle of the forest. It is chilly outside and you haven't eaten for days. Do you want to find shelter or scavenge for food?")
if first == "shelter":
    print("You walk through the forest which filled with thousands of trees, and all sorts of animals and critters.")
    search = input("After a while you stumble upon a cave. Do you go inside for shelter or do you keep searching somewhere else for shelter?")
    if search == "go inside":
        print("You enter in the cave, its dark, quiet and has a strange humidity in the air.")
        cave = input ("Do you want to sleep or explore?")
        if cave == "sleep":
            print("You sleep through the night on the hard rocks inside the cave, it keeps you safe from the elements outside, so that you can find civilization tomorrow. To be continued...")
        elif cave == "explore":
            print("You decided to explore the cave. However, pretty soon you get lost and you're wandering aimlessly in the cave and eventually you pass out from exhaustion. Game over...")

    elif search == "keep looking":
        print("You decided to press forward on the search for shelter for the night. You eventually climb up a tree and sleep in it. Then the next morning you awake to the morning sky. After climbing down from the tree, you wander the vast forest.")
        forest = input("As you wander you see a fire spreading across the forest, what do you do? Do you run away or do you take for cover?")
        if forest == "Run":
            print("You start running away from the forest fire in the hopes that you can get out to avoid the fire. In doing so, you check your phone and you received cell service. While running, you call the closest fire department services and alert them to the forest fire and to your surroundings. The emergency services were able to locate you and within 20 minutes they arrive at your location to fight off as much as the forest fire as they can.")
            print("Hours later, more help arrives and people offer to get you to safety while the fire department does their job. Gladly you accept and they get you to the hospital to check for any injuries. You survived the forest! Congrats! The End...")
        elif forest == "cover":
            print("You decide to take for cover, which shelters you for a little while. However the flames then get to you and engulf you into the intense heat of the forest fire, burning your skin alive.")
            fire = input("Do you run for your life or do you stay there?")
            if fire == "escape":
                print("You run as far as your body will allow with te severe burning on your skin. You barely make it out alive, and emergency services were contacted as a few campers noticed the forest fire. withing 30 miutes they arrive. They put out the fire, meanwhile the medical team loads you onto a stretcher in the ambulance and they rush you to the nearest hospital to treat your severe burns on your skin. You made out alive! The End...")
            elif fire == "stay":
                print("you stay in the fire and you are burned alive. Death then overtakes you. Game Over...")
    
elif first == "food":
    print("You decided you needed to satisfy your hunger first.")
    berry = input("You find some berry bushes, though you're skeptical if theyre safe to eat or not. Will you test your luck or will you choose not to eat them?")
    if berry == "eat":
        print("You test your luck by eating the berries. They tasted delicious, but as you search for shelter for the night, you start to feel dizzy. The nausea takes over you as you realized those berries weren;t safe to eat afterall and you collapse on the ground. Game over...")
    elif berry == "don't eat":
        print("You decide not to eat the berries , and after doing so you found a pack of wolves nearby.")
        wolf = input("Do you appraoch them or go somewhere else?")
        if wolf == "approach":
            print("You approach the pack of wolves, and they turn to be hostile and they attack you. As you fight them off, they overtake you and eat you alive. Game over...")
        elif wolf == "leave":
            print("You walk in the opposite direction. You keep walking for hours until you find a paved road. Hallelujah! You see cars in the road and wave them on and they take you back to the city! You survived! The End...")

else: 
    print("You've completed the Adventure! Thanks for playing!")