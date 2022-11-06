from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        completed = False
        if self.completed_at: 
            completed = True
        
        return{
            "id":self.task_id,
            "title":self.title,
            "description":self.description,
            "is_complete":completed
            }

        








    # '''check default/nullable'''
