from django import forms
from .models import Experience, Training, Achievement


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


INPUT_CLASSES = (
    "w-full bg-panel border border-line rounded-lg px-4 py-2.5 text-sm "
    "text-slate-100 placeholder-slate-500 "
    "focus:border-accent focus:ring-1 focus:ring-accent outline-none transition"
)

TEXTAREA_CLASSES = INPUT_CLASSES

CHECKBOX_CLASSES = (
    "w-4 h-4 rounded border-line bg-panel text-accent "
    "focus:ring-accent focus:ring-offset-0"
)

DATE_CLASSES = (
    "w-full bg-panel border border-line rounded-lg px-4 py-2.5 text-sm "
    "text-slate-100 "
    "focus:border-accent focus:ring-1 focus:ring-accent outline-none transition "
    "[color-scheme:dark]"
)


class ExperienceForm(forms.ModelForm):
    period_start = forms.CharField(
        label="Start Date",
        widget=forms.DateInput(attrs={
            "type": "month",
            "class": DATE_CLASSES,
        }),
    )
    period_end = forms.CharField(
        label="End Date",
        required=False,
        widget=forms.DateInput(attrs={
            "type": "month",
            "class": DATE_CLASSES,
        }),
    )

    class Meta:
        model = Experience
        fields = ["role", "org", "current", "desc"]
        widgets = {
            "role": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. Backend Developer"}),
            "org": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. Zenith International School"}),
            "current": forms.CheckboxInput(attrs={"class": CHECKBOX_CLASSES, "id": "id_current"}),
            "desc": forms.Textarea(attrs={"class": TEXTAREA_CLASSES, "rows": 3, "placeholder": "Describe your role..."}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reorder fields so date pickers appear between org and current
        self.order_fields(["role", "org", "period_start", "period_end", "current", "desc"])

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get("period_start", "")
        current = cleaned.get("current", False)
        end = cleaned.get("period_end", "")

        if not current and not end:
            self.add_error("period_end", "End date is required unless 'Current' is checked.")

        # Format: "May 2025 - Present" or "May 2025 - Dec 2025"
        import datetime
        try:
            start_dt = datetime.datetime.strptime(start, "%Y-%m")
            start_str = start_dt.strftime("%b %Y")
        except (ValueError, TypeError):
            start_str = start

        if current:
            end_str = "Present"
        else:
            try:
                end_dt = datetime.datetime.strptime(end, "%Y-%m")
                end_str = end_dt.strftime("%b %Y")
            except (ValueError, TypeError):
                end_str = end

        cleaned["period"] = f"{start_str} - {end_str}"
        return cleaned

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.period = self.cleaned_data["period"]
        if commit:
            instance.save()
        return instance


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ["title", "issuer"]
        widgets = {
            "title": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. Data Science with Python"}),
            "issuer": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. Simplilearn"}),
        }


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ["name", "year", "result"]
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. BIC Hackathon v1.0"}),
            "year": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. 2023"}),
            "result": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "e.g. 3rd Place"}),
        }
