## Project PAD
In my quest to develop a dynamic NPC (Non-Player Character) system, I aimed for a model capable of exhibiting a wide array of emotional responses without the necessity for explicit programming of each reaction. The core idea was straightforward: by tweaking a few parameters, the NPC could display varied emotional states, leading to distinct interactions, such as different dialogues or actions.

To get this result, I made a Python script leveraging the PAD emotional state model, a framework for characterizing emotions through **Pleasure**, **Arousal**, and **Dominance**. You can find more about the PAD model [here](https://en.wikipedia.org/wiki/PAD_emotional_state_model}. The concept behind this approach is fairly simple, yet it's important to note that the outcomes may not always align perfectly with expected behaviors. For example, an NPC reacting with joy in the midst of a catastrophic event, like an explosion causing casualties, clearly illustrates a misalignment between the intended emotional response and the model's output. Or maybe it does not, and I just created a bunch of psychopathic NPCs, who knows.

Despite these challenges it's a starting point for experimenting with emotional states in NPCs, and I believe it has the potential to maybe add some flair in a project here and there. Feel free to give download the code and try it for yourself.

# Usage
Run a terminal from the project root and type:
```
python3 pad_model.py
```

Adjust **traits** and **stimulus_factors** to get different emotional types and add unique value to **update_emotional_state** to get different results.