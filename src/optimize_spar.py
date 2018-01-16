from sparInstance import SparInstance
import numpy as np
import time

def example_spar():
    myspar = SparInstance()
    #myspar.evaluate('psqp')
    #myspar.visualize('spar-initial.jpg')
    myspar.run('psqp')
    return myspar
    
def psqp_optimal():
    #OrderedDict([('sp.total_cost', array([5.07931743]))])
    myspar = SparInstance()

    myspar.freeboard = 5.10158277e-15
    myspar.fairlead = 71.10786714
    myspar.fairlead_offset_from_shell = 0.89788471
    myspar.section_height = np.array([46.90829885, 47.09591478, 42.98780181, 15.62142311, 27.12647036])
    myspar.outer_radius = np.array([3.42031956, 3.76211996, 4.13833196, 3.74070578, 3.36663524, 3.25 ])
    myspar.wall_thickness = np.array([0.005 , 0.01798306, 0.01634286, 0.0305431 , 0.01614555, 0.02401723])
    myspar.scope_ratio = 3.5943495
    myspar.anchor_radius = 853.84311789
    myspar.mooring_diameter = 0.07110683
    myspar.stiffener_web_height = np.array([0.12446595, 0.11906005, 0.13367389, 0.09986728, 0.20104476])
    myspar.stiffener_web_thickness = np.array([0.00516946, 0.00494494, 0.00555185, 0.01137231, 0.01044597])
    myspar.stiffener_flange_width = np.array([0.01 , 0.01 , 0.01 , 0.02438453, 0.10485385])
    myspar.stiffener_flange_thickness = np.array([0.27895428, 0.3056761 , 0.49283386, 0.11848842, 0.01322849])
    myspar.stiffener_spacing = np.array([0.21985983, 0.40572512, 1.50992577, 2.76799805, 2.87945321])
    myspar.permanent_ballast_height = 30.18703972

    myspar.evaluate('psqp')
    myspar.visualize('spar-psqp.jpg')
    return myspar
    '''
OrderedDict([('freeboard.x', array([5.10158277e-15])), ('fairlead.x', array([71.10786714])), ('fairlead_offset_from_shell.x', array([0.89788471])), ('section_height.x', array([46.90829885, 47.09591478, 42.98780181, 15.62142311, 27.12647036])), ('outer_radius.x', array([3.42031956, 3.76211996, 4.13833196, 3.74070578, 3.36663524,
       3.25      ])), ('wall_thickness.x', array([0.005     , 0.01798306, 0.01634286, 0.0305431 , 0.01614555,
       0.02401723])), ('scope_ratio.x', array([3.5943495])), ('anchor_radius.x', array([853.84311789])), ('mooring_diameter.x', array([0.07110683])), ('stiffener_web_height.x', array([0.12446595, 0.11906005, 0.13367389, 0.09986728, 0.20104476])), ('stiffener_web_thickness.x', array([0.00516946, 0.00494494, 0.00555185, 0.01137231, 0.01044597])), ('stiffener_flange_width.x', array([0.01      , 0.01      , 0.01      , 0.02438453, 0.10485385])), ('stiffener_flange_thickness.x', array([0.27895428, 0.3056761 , 0.49283386, 0.11848842, 0.01322849])), ('stiffener_spacing.x', array([0.21985983, 0.40572512, 1.50992577, 2.76799805, 2.87945321])), ('permanent_ballast_height.x', array([30.18703972]))])
    '''


def conmin_optimal():
    #OrderedDict([('sp.total_cost', array([ 8.15839897]))])
    myspar = SparInstance()
    myspar.freeboard = 5.0
    myspar.fairlead = 7.57
    myspar.fairlead_offset_from_shell = 0.05
    myspar.section_height = np.array([ 18.99987492,  18.9998873 ,  18.99990693,  18.99990914,  18.99990425])
    myspar.outer_radius = np.array([ 6.99962345,  6.99955813,  6.99973629,  6.99978022,  6.99976883, 6.99988])
    myspar.wall_thickness = np.array([ 0.03712666,  0.02787312,  0.02712097,  0.02206188,  0.02157211, 0.03579269])
    myspar.scope_ratio = 2.40997737
    myspar.anchor_radius = 450.0
    myspar.mooring_diameter = 0.1909802
    myspar.stiffener_web_height= np.array([ 0.10557588,  0.10316776,  0.09795284,  0.09743845,  0.09743956])
    myspar.stiffener_web_thickness = np.array([ 0.03599046,  0.03502903,  0.03323707,  0.03302298,  0.0330262 ])
    myspar.stiffener_flange_width = np.array([ 0.10066915,  0.10029873,  0.09894232,  0.09882406,  0.0988245 ])
    myspar.stiffener_flange_thickness = np.array([ 0.02739561,  0.02327079,  0.01406197,  0.01304515,  0.01304842])
    myspar.stiffener_spacing = np.array([ 0.40020418,  0.40036638,  0.4008825 ,  0.4009331 ,  0.40093272])
    myspar.permanent_ballast_height = 10.0

    myspar.evaluate('conmin')
    return myspar
    '''
OrderedDict([('sg.draft_depth_ratio', array([ 0.41284162])), ('mm.safety_factor', array([ 0.7999935])), ('mm.mooring_length_min', array([ 1.03413212])), ('mm.mooring_length_max', array([ 0.76788083])), ('sp.flange_spacing_ratio', array([ 0.25154447,  0.25051738,  0.24681128,  0.24648516,  0.2464865 ])), ('sp.web_radius_ratio', array([ 0.01508315,  0.01473899,  0.01399375,  0.01392023,  0.01392029])), ('sp.flange_compactness', array([ 4.91418164,  4.18969521,  2.56643842,  2.38370799,  2.38429482])), ('sp.web_compactness', array([ 8.20782661,  8.17503344,  8.16979471,  8.16002162,  8.160726  ])), ('sp.axial_local_unity', array([ 0.51507608,  0.46336477,  0.38573459,  0.25387818,  0.06900377])), ('sp.axial_general_unity', array([ 0.9982523 ,  0.95677559,  0.9846294 ,  0.65050248,  0.19042545])), ('sp.external_local_unity', array([ 0.43199964,  0.39057533,  0.32676712,  0.21654406,  0.05750315])), ('sp.external_general_unity', array([ 1.00397317,  0.96693407,  0.99605626,  0.66093149,  0.1917524 ])), ('sp.metacentric_height', array([ 20.55260275])), ('sp.static_stability', array([ 20.41649121])), ('sp.variable_ballast_height', array([ 28.52903672])), ('sp.variable_ballast_mass', array([ 4464694.51334896])), ('sp.offset_force_ratio', array([ 0.98529446])), ('sp.heel_angle', array([ 2.39612487]))])
    '''


def cobyla_optimal():
    #OrderedDict([('sp.total_cost', array([ 6.83851908]))])
    myspar = SparInstance()
    myspar.freeboard = 7.56789854
    myspar.fairlead = 9.41184644
    myspar.fairlead_offset_from_shell = 0.0471558864
    myspar.section_height = np.array([ 18.708914991,  18.784270853,  18.799716693,  18.648435942, 18.711380637])
    myspar.outer_radius = np.array([ 5.764219519,  5.657993694,  6.159558061,  6.125155506, 6.293851894,  6.606570305])
    myspar.wall_thickness = np.array([ 0.043758918  ,  0.03934623132,  0.04101795034,  0.03947006871, 0.03855182803,  0.04268526778])
    myspar.scope_ratio = 2.39202552
    myspar.anchor_radius = 442.036507
    myspar.mooring_diameter = 0.153629334
    myspar.stiffener_web_height= np.array([ 0.1433863028,  0.1192863504,  0.1102913546,   0.0959098443,   0.0760210847])
    myspar.stiffener_web_thickness = np.array([ 0.0059552804,  0.0049543342,  0.004580744 ,  0.003983435 ,  0.0031573928 ])
    myspar.stiffener_flange_width = np.array([ 0.0924192057,  0.0977347306,  0.0800589589,  0.0797488027,  0.0861943184 ])
    myspar.stiffener_flange_thickness = np.array([ 0.02739561,  0.02327079,  0.01406197,  0.01304515,  0.01304842])
    myspar.stiffener_spacing = np.array([ 0.937472777,   0.913804583,   0.975992681,   0.940785141,  1.077950861])
    myspar.permanent_ballast_height = 2.1531719

    myspar.evaluate('cobyla')
    return myspar
    '''
OrderedDict([('sg.draft_depth_ratio', array([ 0.3948845])), ('mm.safety_factor', array([ 0.79998459])), ('mm.mooring_length_min', array([ 1.03296286])), ('mm.mooring_length_max', array([ 0.76687562])), ('sp.flange_spacing_ratio', array([ 0.09858335,  0.10695364,  0.08202824,  0.08476835,  0.07996127])), ('sp.web_radius_ratio', array([ 0.02510657,  0.020188  ,  0.01795587,  0.01544565,  0.01178583])), ('sp.flange_compactness', array([ 4.34435796,  3.92278448,  4.35797943,  2.16402123,  1.        ])), ('sp.web_compactness', array([ 1.,  1.,  1.,  1.,  1.])), ('sp.axial_local_unity', array([ 0.47642979,  0.38788415,  0.28705696,  0.17106678,  0.05175507])), ('sp.axial_general_unity', array([ 0.97397846,  0.97695689,  0.98037179,  0.98931662,  0.5567153 ])), ('sp.external_local_unity', array([ 0.41057698,  0.33470586,  0.24904213,  0.14822411,  0.04496548])), ('sp.external_general_unity', array([ 1.        ,  1.        ,  1.        ,  1.        ,  0.56070475])), ('sp.metacentric_height', array([ 6.12375997])), ('sp.static_stability', array([ 5.98379185])), ('sp.variable_ballast_height', array([ 60.25812533])), ('sp.variable_ballast_mass', array([ 6785190.91932651])), ('sp.offset_force_ratio', array([ 1.0000217])), ('sp.heel_angle', array([ 9.99999845]))])
    '''
        
if __name__ == '__main__':
    example_spar()
    #psqp_optimal()