from app.api import bp 

@bp.route('/blogs/<int:id>', methods=['GET'])
def get_blog(id):
    pass

@bp.route('/blogs', methods=['GET'])
def get_blogs():
    pass

@bp.route('/blogs', methods=['POST'])
def create_blog():
    pass


@bp.route('/blogs/<int:id>', methods=['PUT'])
def update_blog(id):
    pass
