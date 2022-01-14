from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import Projects, Tag
from .forms import ProjectsForm, ReviewForm
from .utils import searcProject, paginateProjects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def projects(request):
    projects, search_query = searcProject(request)
    custom_range, projects = paginateProjects(request, projects)
    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    form = ReviewForm()
    projectObj = Projects.objects.get(id=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)
    context = {
        'form': form,
        'project': projectObj,
    }
    return render(request, 'projects/single-projects.html', context)


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/projects_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    form = ProjectsForm(instance=project)
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/projects_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'delete_template.html', context)
