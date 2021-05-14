# Exercises of Condensed Matter

## Assignment 1

* May 14, 2021

### Question 1

The Sommerfeld theory of metals improves upon the Drude theory of metals in which Drude applied the highly successful kinetic theory of gases to a metal, which was considered as a gas of electrons. Explain how the improvement was achieved and describe shortcomings of Sommerfeld’s theory.

* Answer:

    Many properties of the free electron model follow directly from equations related to the Fermi gas, as the independent electron approximation leads to an ensemble of non-interacting electrons. For a three-dimensional electron gas we can define the Fermi energy as:
    $$E_{\rm F} = \frac{\hbar^2}{2m_e}\left(3\pi^2n\right)^\frac{2}{3}$$

    The Fermi energy defines the energy of the highest energy electron at zero temperature. For metals the Fermi energy is in the order of units of electronvolts above the free electron band minimum energy.

    The 3D density of states (number of energy states, per energy per volume) of a non-interacting electron gas is given by:
    $$g(E) = \frac{m_e}{\pi^2\hbar^3}\sqrt{2m_eE} = \frac{3}{2}\frac{n}{E_{\rm F}}\sqrt{\frac{E}{E_{\rm F}}}$$

    where $E \geq 0$ is the energy of a given electron. This formula takes into account the spin degeneracy but does not consider a possible energy shift due to the bottom of the conduction band. For 2D the density of states is constant and for 1D is inversely proportional to the square root of the electron energy.

    The chemical potential $μ$ of electrons in a solid is also known as the Fermi level and, like the related Fermi energy, often denoted $E_{\rm F}$ . The Sommerfeld expansion can be used to calculate the Fermi level ($T > 0$) at higher temperatures as:
    $$E_{\rm F}(T) = E_{\rm F}(T=0) \left[1 - \frac{\pi ^2}{12} \left(\frac{T}{T_{\rm F}}\right) ^2 - \frac{\pi^4}{80} \left(\frac{T}{T_{\rm F}}\right)^4 + \cdots \right]$$

    where $T$ is the temperature and we define $T_{\rm F}=E_{\rm F}/k_{\rm B}$ as the Fermi temperature $k_{\rm B}$ is Boltzmann constant). The perturbative approach is justified as the Fermi temperature is usually of about $10^5 {\rm K}$ for a metal, hence at room temperature or lower the Fermi energy $E_{\rm {F}}(T=0)$ and the chemical potential $E_{\rm {F}}(T>0)$ are practically equivalent.

    Although the Sommerfeld model explains a bit about metals, it is still incomplete.

  * Temperature dependence  
    The free electron model presents several physical quantities that have the wrong temperature dependence, or no dependence at all like the electrical conductivity. The thermal conductivity and specific heat are well predicted for alkali metals at low temperatures, but fails to predict high temperature behaviour coming from ion motion and phonon scattering.

  * Hall effect and magnetoresistance
    The Hall coefficient has a constant value $R_{\rm H}=–1/(ne)$ in Drude's model and in the free electron model. This value is independent of temperature and the strength of the magnetic field. The Hall coefficient is actually dependent on the band structure and the difference with the model can be quite dramatic when studying elements like magnesium and aluminium that have a strong magnetic field dependence. The free electron model also predicts that the traverse magnetoresistance, the resistance in the direction of the current, does not depend on the strength of the field. In almost all the cases it does.

  * Directional
    The conductivity of some metals can depend of the orientation of the sample with respect to the electric field. Sometimes even the electrical current is not parallel to the field. This possibility is not described because the model does not integrate the crystallinity of metals, i.e. the existence of a periodic lattice of ions.

  * Diversity in the conductivity
    Not all materials are electrical conductors, some do not conduct electricity very well (insulators), some can conduct when impurities are added like semiconductors. Semimetals, with narrow conduction bands also exist. This diversity is not predicted by the model and can only by explained by analysing the valence and conduction bands. Additionally, electrons are not the only charge carriers in a metal, electron vacancies or holes can be seen as quasiparticles carrying positive electric charge. Conduction of holes leads to an opposite sign for the Hall and Seebeck coefficients predicted by the model.

### Question 2

The density of copper is $8.92\times10^3{\rm kg/m^3}$. The resistivity is $1.73\times10^{-8}{\rm Ω·m}$ and the weight of a copper atom is $63.5 {\rm amu}$ (atomic mass unit). (i) Assuming each Cu atom contributes one conduction electron, calculate the electron mobility and the average time between collisions (relaxation time).(ii) Calculate the Fermi energy, Fermi wave vector, Fermi velocity and Fermi temperature.

* Answer:

  * (i)

    We know:  
    Density of Cu: $D_{\rm Cu}=8.92\times10^3{\rm kg/m^3}$,  
    Resistivity of Cu: $ρ_{\rm Cu}=1.73\times10^{-8}{\rm Ω·m}$,  
    Weight of a copper atom: $6.023 {\rm amu}$

    We can get the number of atoms that $1{\rm g}$ Cu contains:
    $$D_{\rm N} = 6.023\times10^{23}/63.5$$
    and, the atom density of Cu:
    $$n_{\rm Cu} = N \times D \approx 8.46\times10^{28} {\rm atoms/m^3}$$

    Given, there is 1 conduction $e^-$ contributed per Cu atom. The free electron density equals $n_{\rm Cu}$. From Drude's model, we have the relation between conductivity and free electron density: $σ=neμ$. We can get: $μ=σ/(ne)=1/(ρne)=4.24\times10^3{\rm m^2/vs}$.

    Then, we can compute the relaxation time via the relation it obeys:
    $$τ=\frac{m_{\rm e}μ}{e}\approx 2.43\times 10^{-14}{\rm s}$$

  * (ii)

    We have the expression for Fermi energy:
    $$E_\text{F} = \frac{\hbar^2}{2m_0} \left( \frac{3 \pi^2 N}{V} \right)^{2/3}$$

    We can get the relation:
    $$E_{\rm F}=\frac{2(π\hbar)^2}{m}\left(\frac{3N_{\rm Cu}}{8πV}\right)^{2/3}=\frac{2(π\hbar)^2}{m}\left(\frac{3n_{\rm Cu}}{8π}\right)^{2/3}\approx7.03{\rm eV}$$

    In terms of the Fermi wave vector obeys:
    $$E_{\rm F}=\frac{\hbar^2}{2m}k_{\rm F}^2$$

    So, we can get:
    $$k_{\rm F}=\sqrt{\frac{2mE_{\rm F}}{\hbar^2}}\approx1.36\times10^{10}{\rm m^{-1}}$$

    For Fermi velocity, we have:
    $$E_{\rm F}=\frac{1}{2}mv_{\rm F}^2$$

    So, we can compute the Fermi velocity:
    $$v_{\rm F}=\sqrt{\frac{2E_{\rm F}}{m}}\approx1.57\times10^6{\rm m·s^{-1}}$$

    For Fermi temperature, $T_{\rm F}$ obeys:
    $$k_{\rm B} T_{\rm F}=E_{\rm F}$$

    So, we can get the Fermi temperature:
    $$T_{\rm F}=\frac{E_{\rm F}}{k_{\rm B}}\approx8.15×10^4{\rm K}$$

### Question 3

Sodium atoms occupy a volume of $4×10^{-29}{\rm m^3}$. Each atom contributes one free conduction electron. Calculate the Fermi velocity of sodium and compare it to that of copper above.

* Answer:

    We can get the electron density per mole of Sodium:
    $$n=\frac{1}{V_{\rm atom}}×N_{\rm A}\approx1.51×10^{52}$$

    The Fermi velocity and Fermi momentum have the following relationship:
    $$v_{\rm F}=\frac{p_{\rm F}}{m_e}=\frac{\hbar k_{\rm F}}{m_e}=\frac{\hbar}{m_e}(3π^2n)^{1/3}≈0.87×10^{13}{\rm m·s^{-1}}$$

### Question 4

i. A face-centred-cubic lattice with conventional cubic cell has a side length $a$. Determine its reciprocal lattice unit cell (first Brillouin zone) and reciprocal lattice vectors.

* Answer

  * Lattice vectors of FCC core:
    $$a_1=\frac{a}{2}(\hat k+\hat i)$$
    $$a_2=\frac{a}{2}(\hat i+\hat j)$$
    $$a_3=\frac{a}{2}(\hat j+\hat k)$$

  * Reciprocal lattice vectors core given by:
    $$b_1=2π\frac{a_2×a_3}{a_1·(a_2×a_3)}=\frac{2π}{a}(\hat k-\hat j+\hat i)$$
    $$b_2=2π\frac{a_3×a_1}{a_1·(a_2×a_3)}=\frac{2π}{a}(\hat i-\hat k+\hat j)$$
    $$b_3=2π\frac{a_1×a_2}{a_1·(a_2×a_3)}=\frac{2π}{a}(\hat j-\hat i+\hat K)$$

ii. A hexagonal lattice has lattice constants $a$ and $c$. Determine its reciprocal lattice unit cell and reciprocal lattice vectors. In both cases show full working.

* Answer
