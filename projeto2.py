# Primeiro, precisamos carregar os módulos, onde o pylab é a junção do pyplot com o numpy.
from pylab import plot, show, ylim, xlim, xlabel, ylabel, grid, scatter, legend
# Para converter os dados de coordenadas polares para cartesianas, 
# vamos precisar das funções seno e cosseno.
from math import cos, sin, pi

######################################################################################################
########### P R O J E T O   P Y T H O N   2  -  A P O L L O, B E R N A R D  E  M I G U E L ###########   
######################################################################################################

# Estamos usando o sistema CGS de unidades.

# Vamos precisar da constante gravitacional gaussiana.
k = 0.01720209395
# Vamos usar a constante gravitacional heliocêntrica.
GM = k**2

# Precisamos definir as condições iniciais. 
# As distâncias são dadas em unidades astronômicas e o tempo em dias.

# Distância do Sol a Terra (UA). 
r = 1.0 
# Ângulo provindo da mudança de coordenadas: cartesianas para polares (rad). 
theta = - pi/2
# Velocidade de translação (rad*UA/dias).
v = 0.0
# Velocidade angular (rad/dias).
omega = 2*pi/365.25

# Variando apenas os valores de v, a energia mecânica do sistema mudará.
# Sendo assim, podemos verificar como tal mudança afeta na trajetória do planeta.
# Com isso, a massa dele torna-se "irrelevante" podendo ser igual a 1 sem perda de generalidade física.

# O momento angular é uma constante de movimento.
L = omega*r**2

# Energia mecânica do sistema:
# Se E > 0, então a órbita será aberta;
# Se E < 0, a orbita será fechada.
Energia = 0.5*(v**2 + (L/r)**2) - GM/r

# Para os gráficos em coordenadas cartesianas (x,y),
# temos que preparar as listas x e y, 
# as quais são inicialmente vazias.
x = [ ]
y = [ ]

# Definimos o passo de integração. 
dt = 0.01

# Para órbitas fechadas, basta percorrer uma volta.
theta_inicial = theta
theta_final = theta_inicial + 2*pi

# Por enquanto, o cálculo é para órbitas fechadas.
if (Energia < 0):
    while(theta < theta_final):
        # Aceleração total.
        a = (L**2)/(r**3) - GM/(r**2)
        v += a*dt
        r += v*dt
        omega = L/r**2
        theta += omega*dt
        # Transformamos (r, theta) para (x,y), onde a função append faz tal transformação
        # e preenchemos as listas x e y.
        x.append(r*cos(theta))
        y.append(r*sin(theta))

plot(x,y, label = "Energia A")

'''
# Calculo analítico, para comparação. 
x = []
y = []
theta = 0
# A = (L/m*k)**2.
A = 1.0
# Excentricidade da órbita (Para órbitas elípticas, 0 < epsilon < 1).
epsilon = 0.01

print("epsilon: ", epsilon)

if (Energia < 0):
    while (theta < 2*pi):
        # Equação da trajetória.
        r = A/(1 + epsilon*cos(theta))
        theta += 0.01
        x.append(r*cos(theta))
        y.append(r*sin(theta))

plot(x,y, label = "Cálculo Analítico")
'''

##################################################################################################################
#################### PODEMOS REPETIR OS CÁLCULOS ACIMA, PORÉM COM OUTROS PARÂMETROS INICIAIS  ####################
##################################################################################################################

# Condições iniciais (distâncias em UA e tempo em dias).
# m = 1.
r = 1.0
theta = - pi/2
v = 0.009
omega = 2*pi/365.25
L = omega*r**2
Energia = 0.5*(v**2 + (L/r)**2) - GM/r
x = []
y = []
dt = 0.01
theta_inicial = theta
theta_final = theta_inicial + 2*pi

if (Energia < 0):
    while(theta < theta_final):
        a = (L**2)/(r**3) - GM/(r**2)
        v += a*dt
        r += v*dt
        omega = L/r**2
        theta = theta + omega*dt
        x.append(r*cos(theta))
        y.append(r*sin(theta))

#Preparativos para o gráficos
lim_max = max([max(x), max(y)])
lim_max = 1.10*lim_max  # Para que a curva não toque a borda
lim_min = -1*lim_max    # Para que os eixos x e y tenham o mesmo tamanho
ylim(lim_min, lim_max)
xlim(lim_min, lim_max)
xlabel("x (UA)")
ylabel("y (UA)")
plot(x,y, label = "Energia B")
# Colocamos o Sol no posição x = 0, y = 0, s = tamanho do ponto, c = cor e alpha = 0 -- transparente, 1 -- opaco.
scatter(0,0, s = 200, c = 'yellow', alpha = 0.8)
# Escrevemos a legenda dos gráficos na figura em uma posição determinada (loc = 2).
legend(loc = 2)
# Cria uma grade linhas horizontais e verticais na figura (grid()).
grid()
show()
