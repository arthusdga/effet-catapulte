vln=[1/v[i] for i in range(len(v))]

# Ajustement de la régression linéaire
coefficients = np.polyfit(vln, T, 1, 90) # Le degré 1 indique une régression linéaire

pente, intercept = coefficients
droite=[pente*vln[i]+intercept for i in range(len(vln))]

correlation=np.corrcoef(T,droite)[0][1]

print(f"Pente : {pente}")
print(f"Ordonnée à l'origine : {intercept}")
print(f"coefficient de correlation : {correlation}")

plt.plot(vln, droite, label="T(Δv)", color="red", linestyle="-")
plt.plot(vln, T, label="T(Δv)", color="blue", linestyle="-")
plt.title("evolution du temps de transfert en fonction du deltav total")
plt.xlabel("Axe Δv")
plt.ylabel("Axe T")
#plt.xscale('log')
plt.legend()
plt.grid(True)
plt.show()

