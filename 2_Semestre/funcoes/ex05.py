def voter_classification(age):
    voter_status = "Não-eleitor" if age < 16 else "Eleitor obrigatório"
    
    if age >= 16 and age <= 18 or age > 65:
        return "Eleitor Facultativo"

    return voter_status


print(voter_classification(15))
print(voter_classification(16))
print(voter_classification(18))
print(voter_classification(20))
print(voter_classification(65))
print(voter_classification(70))