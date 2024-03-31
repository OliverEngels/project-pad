class PADModel:
    def __init__(self, **personality_traits):
        self.pleasure = 0
        self.arousal = 0
        self.dominance = 0
        self.personality_traits = personality_traits

        self.emotion_ranges = [
            {'name': 'Happiness', 'P': (0.5, 1), 'A': (0, 1), 'D': (0, 1)},
            {'name': 'Sadness', 'P': (-1, -0.5), 'A': (-1, 0), 'D': (-1, 1)},
            {'name': 'Anger', 'P': (-1, -0.5), 'A': (0.5, 1), 'D': (-1, 1)},
            {'name': 'Fear', 'P': (-1, -0.5), 'A': (0.5, 1), 'D': (-1, -0.5)},
            {'name': 'Relaxation', 'P': (0.5, 1), 'A': (-1, 0), 'D': (-1, 1)},
            {'name': 'Excitement', 'P': (0.5, 1), 'A': (0.5, 1), 'D': (0, 1)},
            {'name': 'Boredom', 'P': (-1, -0.5), 'A': (-1, 0), 'D': (0.5, 1)},
            {'name': 'Frustration', 'P': (-1, -0.5), 'A': (0.5, 1), 'D': (-0.5, 0.5)},
            {'name': 'Contentment', 'P': (0.5, 1), 'A': (-0.5, 0.5), 'D': (0.5, 1)},
            {'name': 'Anxiety', 'P': (-1, -0.5), 'A': (0.5, 1), 'D': (-0.5, 0.5)},
            {'name': 'Surprise', 'P': (-0.5, 0.5), 'A': (0.5, 1), 'D': (-1, 1)},
            {'name': 'Disgust', 'P': (-1, -0.5), 'A': (-0.5, 0.5), 'D': (-1, 1)},
            {'name': 'Curiosity', 'P': (0, 1), 'A': (0, 1), 'D': (0, 1)},
            {'name': 'Indifference', 'P': (-0.5, 0.5), 'A': (-1, 0), 'D': (-1, 1)},
            {'name': 'Confidence', 'P': (0.5, 1), 'A': (0, 0.5), 'D': (0.5, 1)},
            {'name': 'Shame', 'P': (-1, -0.5), 'A': (-0.5, 0.5), 'D': (-1, -0.5)},
            {'name': 'Jealousy', 'P': (-1, -0.5), 'A': (0, 0.5), 'D': (-1, -0.5)},
            {'name': 'Envy', 'P': (-1, -0.5), 'A': (0, 0.5), 'D': (-1, -0.5)},
            {'name': 'Sympathy', 'P': (0, 1), 'A': (-1, 0), 'D': (-1, 1)},
            {'name': 'Pride', 'P': (0.5, 1), 'A': (0, 0.5), 'D': (0.5, 1)}
        ]

    def update_emotional_state(self, pleasure_change, arousal_change, dominance_change, stimulus):
        arousal_change += self.personality_traits.get('Adve_Caut', 0) * stimulus.get('excitement_factor', 0)
        arousal_change += self.personality_traits.get('Extr_Intr', 0) * stimulus.get('social_factor', 0)
        arousal_change += self.personality_traits.get('Curi_Indi', 0) * stimulus.get('curiosity_factor', 0)
        
        dominance_change += self.personality_traits.get('Prou_Humb', 0) * stimulus.get('achievement_factor', 0)
        dominance_change += self.personality_traits.get('Dete_Flex', 0) * stimulus.get('challenge_factor', 0)
        dominance_change += self.personality_traits.get('Stub_Acco', 0) * stimulus.get('conflict_factor', 0)
        
        pleasure_change += self.personality_traits.get('Know_Naiv', 0) * stimulus.get('learning_factor', 0)
        pleasure_change += self.personality_traits.get('Opti_Pess', 0) * stimulus.get('positive_factor', 0)
        pleasure_change += self.personality_traits.get('Witt_Seri', 0) * stimulus.get('humor_factor', 0)

        self.pleasure = max(min(self.pleasure + pleasure_change, 1), -1)
        self.arousal = max(min(self.arousal + arousal_change, 1), -1)
        self.dominance = max(min(self.dominance + dominance_change, 1), -1) 

    def map_to_emotion(self):
        for emotion_range in self.emotion_ranges:
            if (emotion_range['P'][0] <= self.pleasure <= emotion_range['P'][1] and
                emotion_range['A'][0] <= self.arousal <= emotion_range['A'][1] and
                emotion_range['D'][0] <= self.dominance <= emotion_range['D'][1]):
                return emotion_range['name']
        return 'Neutral'

# (-1 to 1)
traits = {
    # Arousal
    'Adve_Caut': -0.7, # Adventurous vs Cautious
    'Extr_Intr': 0.7, # Extrovert vs Introvert
    'Curi_Indi': -0.4, # Curious vs Indifferent

    # Dominance
    'Prou_Humb': -0.7, # Proud vs Humble
    'Dete_Flex': 0.6, # Determined vs Flexible
    'Stub_Acco': 0.6, # Stubborn vs Accommodating

    # Pleasure
    'Know_Naiv': -0.9, # Knowledgeable vs Naive
    'Opti_Pess': 0.6, # Optimistic vs Pessimistic
    'Witt_Seri': 0.5  # Witty vs Serious
}
pad_model = PADModel(**traits)

# (0 to 1)
stimulus_factors = {
    # Arousal
    'excitement_factor': 0.9,
    'social_factor': 0.5,
    'curiosity_factor': 0.3,

    # Dominance
    'achievement_factor': 0.2,
    'challenge_factor': 0.8,
    'conflict_factor': 0.7,

    # Pleasure
    'learning_factor': 0.4,
    'positive_factor': 0.1,
    'humor_factor': 0.2,
}
pad_model.update_emotional_state(-0.4, 0.3, -0.6, stimulus_factors)

print("Current Emotion:", pad_model.map_to_emotion())
print("Current Pleasure:", pad_model.pleasure)
print("Current Arousal:", pad_model.arousal)
print("Current Dominance:", pad_model.dominance)