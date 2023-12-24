import clingo

program = """
% Define the diseases
disease("Asthma").
disease("Bronchitis").
disease("Chronic Obstructive Pulmonary Disease (COPD)").
disease("Pneumonia").
disease("Tuberculosis").

% Define the symptoms of each disease
symptom("Coughing").
symptom("Shortness of breath").
symptom("Chest tightness").
symptom("Chest pain").
symptom("Fatigue").
symptom("Fever").
symptom("Weight loss").
symptom("Night sweats").

% Define the causes of each disease
causes("Asthma", "Coughing").
causes("Asthma", "Shortness of breath").
causes("Asthma", "Chest tightness").
causes("Bronchitis", "Coughing").
causes("Bronchitis", "Chest pain").
causes("Bronchitis", "Fatigue").
causes("Chronic Obstructive Pulmonary Disease (COPD)", "Coughing").
causes("Chronic Obstructive Pulmonary Disease (COPD)", "Shortness of breath").
causes("Chronic Obstructive Pulmonary Disease (COPD)", "Chest pain").
causes("Pneumonia", "Coughing").
causes("Pneumonia", "Fever").
causes("Pneumonia", "Chest pain").
causes("Tuberculosis", "Weight loss").
causes("Tuberculosis", "Night sweats").

% Define a rule to set the symptom based on command-line input
symptom(S) :- { S }, symptom(S).
% Define a rule to determine the likely diseases based on symptoms
likely_disease(D) :- 
    disease(D), 
    #count { S : symptom(S), causes(D, S) } > 0.

#show likely_disease/1.
"""

symptom = "Fever"
ctl = clingo.Control()
parsed_program, error = clingo.parse_program(program)
ctl.add(parsed_program)
ctl.add(clingo.Function("symptom", [symptom]))
ctl.ground([("base", [])])
with ctl.solve(yield_=True) as handle:
    for model in handle:
        if model.satisfiable:
            print(f"Likely diseases for {symptom}:")
            for atom in model.symbols(shown=True):
                if atom.name == "likely_disease":
                    print(atom.arguments[0])


