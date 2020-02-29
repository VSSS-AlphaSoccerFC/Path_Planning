import pf
import epf

import time

# 1.5 * 1.3

####################
f = epf.EuclidField(
    (75, 65),   # width x height
    (20, 60),    # goal
    [           # obstacles
       (50,50),
       (37, 32),
       (32, 32)
    ]
)
src = (50, 32)
####################

start = time.time()
print("starting")

path = pf.find_path(f, src, f.dst, 100)
next_point = pf.find_path_sample(f, src, f.dst, 100, 0.1)

end = time.time()

print(f'Delta time: {end - start}')

print(f)
im = pf.field_to_image(f)
pf.draw_path(im, path, next_point)
im.save('out.png')


