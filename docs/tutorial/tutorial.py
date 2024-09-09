# %% [markdown]
# # Mockup tutorial

# %%
from mockup import mockup

# %%
mockup.add_one(-11)

# %%
list(mockup.flatten_ints([[9, 11], [12], [4, 5]]))

# %%
c2 = mockup.Circle.from_circumference(100)
round(c2.radius, 3)

# %%
c2  # repr

# %% [markdown]
#
