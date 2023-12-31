# -*- coding: utf-8 -*-pack
{
    # App information
    'name': 'School Management',
    'category': '',
    'version': '16.0',
    'summary': """ School Management System""",
    'description': """ Module is school manage system """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/student_record_sequence.xml',
        'data/student_fees_sequence.xml',
        'data/school_faculty_sequence.xml',
        'views/student_record_view.xml',
        'views/student_list_view.xml',
        'views/student_fees_view.xml',
        'views/school_faculty_view.xml',
        'views/subject_tags_view.xml',
        'views/student_fees_status_view.xml',

    ],
    'images': ['static/description/icon.png'],
    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'price': '101',
    # 'currency': 'EUR',
    'license': 'LGPL-3',
}
