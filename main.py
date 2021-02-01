import coordinates as co
import cv_gen
import msm_gen

def start():
    print('Start')
    print('Coordinates start - {0}, end - {1}'.format(co.get_coors()[:2], co.get_coors()[2:]))
    cv_gen.set_pos_coors(co.get_coors()[0],co.get_coors()[1],co.get_coors()[2],co.get_coors()[3])
    screen = cv_gen.get_shoot()
    # cv_gen.show_screen(screen)
    cv_gen.foo(screen)
    print('End')
    # msm_gen.start_bot()
    # msm_gen.echo_all('test20122')


if __name__ == '__main__':
    start()
