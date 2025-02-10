Visualize commits in a tree like structure:

```git
git log --graph --decorate --oneline
```

Revert the last commit already pushed to remote:

```git
git reset HEAD^ --hard
git push origin -f
```

# Branches
One good way to manage branches when working with multiple things in same projects is following:

## Without absolute path
![[branches.png]]

![](branches.png)

![[../../Assets/branches.png]]

## With Absolute Path
![](../../Assets/branches.png)

# LaTeX Examples

```latex
\begin{equation}
\begin{split}
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} &= 0 \\
\frac{\partial^2 u}{\partial x^2} &= \frac{\partial^2 u}{\partial y^2}
\end{split}
\end{equation}
```

$$R = \frac{V_R}{I}$$

$$R = \frac{2.913}{7.087} = 0.41 \Omega$$

$$dB \propto \frac{i dl sin\theta}{r^2}$$

$$dB = k \frac{i dl sin\theta}{r^2}$$

$$dB = \frac{\mu_o}{4\pi} \frac{i dl sin\theta}{r^2}$$

In vector form,

$$dB = \frac{\mu_o}{4\pi} \frac{i \vec{dl} * \vec{r}}{r^2}$$
