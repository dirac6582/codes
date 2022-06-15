

# https://github.com/phonopy/phonopy/blob/develop/phonopy/phonon/band_structure.py
def get_band_qpoints_by_seekpath(primitive, npoints, is_const_interval=False):
    “””q-points along BZ high symmetry paths are generated using seekpath.
    Parameters
    ----------
    primitive : PhonopyAtoms
        Primitive cell.
    npoints : int
        Number of q-points sampled along a path including end points.
    is_const_interval : bool, optional
        When True, q-points are sampled in a similar interval. The longest
        path length divided by npoints including end points is used as the
        reference interval. Default is False.
    Returns
    -------
    bands : List of ndarray
        Sets of qpoints that can be passed to phonopy.set_band_structure().
        shape of each ndarray : (npoints, 3)
    labels : List of pairs of str
        Symbols of end points of paths.
    connections : List of bool
        This gives one path is connected to the next path, i.e., if False,
        there is a jump of q-points. Number of elements is the same at
        that of paths.
    “””
    try:
        import seekpath
    except ImportError:
        raise ImportError(“You need to install seekpath.”)

    band_path = seekpath.get_path(primitive.totuple())
    point_coords = band_path[“point_coords”]
    qpoints_of_paths = []
    if is_const_interval:
        reclat = np.linalg.inv(primitive.cell)
    else:
        reclat = None
    band_paths = [
        [point_coords[path[0]], point_coords[path[1]]] for path in band_path[“path”]
    ]
    npts = _get_npts(band_paths, npoints, reclat)
    for c, path in enumerate(band_path[“path”]):
        q_s = np.array(point_coords[path[0]])
        q_e = np.array(point_coords[path[1]])
        band = [q_s + (q_e - q_s) / (npts[c] - 1) * i for i in range(npts[c])]
        qpoints_of_paths.append(band)
    labels, path_connections = _get_labels(band_path[“path”])

    return qpoints_of_paths, labels, path_connections
