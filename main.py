import coordinates as co
import cv_fullscreen as cv_full
import cv_gen
import msm_gen


def start():
    print('Start')
    # print('Coordinates start - {0}, end - {1}'.format(co.get_coors()[:2], co.get_coors()[2:]))
    # cv_gen.set_pos_coors(co.get_coors()[0],co.get_coors()[1],co.get_coors()[2],co.get_coors()[3])
    print('Coordinates start - {0}, end - {1}'.format(cv_full.get_coordinates()[:2], cv_full.get_coordinates()[2:]))

    cv_gen.set_pos_coors(cv_full.get_coordinates()[0], cv_full.get_coordinates()[1], cv_full.get_coordinates()[2],
                         cv_full.get_coordinates()[3])

    screen = cv_gen.get_shoot()
    # print(screen)
    # cv_gen.show_screen(screen)
    cv_gen.foo(screen)
    print('End')
    # msm_gen.start_bot()
    # msm_gen.echo_all('test20122')


if __name__ == '__main__':
    start()
