investissement = 1000                                                  
rendement = 10                                                           
gain = (investissement*rendement) / 100                               
print(f"Les gains annuels sont de {gain} euros par an")

investissement += 5000 + gain                                           
rendement += 2                                                             
gain = (investissement*rendement) / 100                                   
print(f"Les nouveaux gains sont de {gain} euros")

investissement = investissement + gain                                    
investissement = investissement - ((investissement*10)/100)               
rendement -= 1                                                            
gain = (investissement*rendement) / 100                                     
print(f"Les gains finaux sont de {gain} euros")

